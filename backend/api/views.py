from datetime import datetime

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from filters import IngredientFilter, RecipeFilter
from recipes.models import (
    Favorite,
    Ingredient,
    IngredientInRecipe,
    Recipe,
    ShoppingCart,
    Tag,
)
from pagination import CustomPagination
from permissions import IsAdminAuthorOrReadOnly
from serializers import (
    IngredientSerializer,
    RecipeReadSerializer,
    RecipeWriteSerializer,
    TagSerializer,
)


class TagViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Вьюсет для модели тега.
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminAuthorOrReadOnly,)


class IngredientViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Вьюсет для модели ингридиента.
    """

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = IngredientFilter


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели рецепта.
    """

    queryset = Recipe.objects.select_related("author").prefetch_related(
        "tags", "favorites", "shopping_cart", "ingredients_in_recipe__ingredient"
    )
    permission_classes = (IsAdminAuthorOrReadOnly,)
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return RecipeReadSerializer

        return RecipeWriteSerializer

    @action(
        detail=True,
        methods=["post", "delete"],
        permission_classes=[IsAuthenticated],
    )
    def favorite(self, request, pk):
        """Метод для добавления/удаления из избранного."""
        recipe = get_object_or_404(Recipe, pk=pk)
        model = Favorite.objects.filter(recipe=recipe, user=request.user)
        if request.method == "POST":
            if not model.exists():
                Favorite.objects.create(recipe=recipe, user=request.user)
            return Response(status=status.HTTP_201_CREATED)

        else:
            if model.exists():
                model.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["post", "delete"],
        permission_classes=[IsAuthenticated],
    )
    def shopping_cart(self, request, pk):
        """Метод для добавления/удаления из списка покупок."""
        recipe = get_object_or_404(Recipe, pk=pk)
        model = ShoppingCart.objects.filter(recipe=recipe, user=request.user)
        if request.method == "POST":
            if not model.exists():
                ShoppingCart.objects.create(recipe=recipe, user=request.user)
            return Response(status=status.HTTP_201_CREATED)

        else:
            if model.exists():
                model.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        permission_classes=[IsAuthenticated],
    )
    def download_shopping_cart(self, request):
        """Метод для скачивания списка покупок."""
        ingredients = (
            IngredientInRecipe.objects.filter(recipe__shopping_cart__user=request.user)
            .values("ingredient__name", "ingredient__measurement_unit")
            .annotate(amount=Sum("amount"))
        )
        shopping_list = [
            f"- {ingredient['ingredient__name']} ({ingredient['ingredient__measurement_unit']}) - {ingredient['amount']}"
            for ingredient in ingredients
        ]
        today = datetime.today().strftime("%Y-%m-%d")
        shopping_list = [" ".join(shopping_list)]
        filename = f"{request.user.username}_shopping_list_{today}.txt"
        response = HttpResponse(shopping_list, content_type="text/plain; charset=UTF-8")
        response["Content-Disposition"] = f"attachment; filename={filename};"
        return response
