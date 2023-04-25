from rest_framework.permissions import SAFE_METHODS, BasePermission

from users.models import UserRole


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return (request.method in SAFE_METHODS
                or request.user.role == UserRole.ADMIN)


class IsAdminAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method in ('GET',)
                or obj.author == request.user
                or request.user.role == UserRole.ADMIN)

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
