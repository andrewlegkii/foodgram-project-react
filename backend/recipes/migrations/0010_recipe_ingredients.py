# Generated by Django 3.2.16 on 2022-10-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20221021_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='recipes.IngredientInRecipe', verbose_name='Ингредиенты в рецепте'),
        ),
    ]
