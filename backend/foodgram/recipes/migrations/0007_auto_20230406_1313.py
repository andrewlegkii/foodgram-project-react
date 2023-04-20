# Generated by Django 2.2.16 on 2023-04-06 08:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20230405_2334'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favorite',
            name='unique_favorite',
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, null=True, validators=[django.core.validators.RegexValidator('^#([a-fA-F0-9]{6})', message='Введите HEX-код цвета.')], verbose_name='Цвет в HEX'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_-]+$', message='Разрешены буквы, цифры, тире и знаки подчеркивания.')], verbose_name='Название'),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_user_fav_recipe'),
        ),
    ]
