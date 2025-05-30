# Generated by Django 5.1.7 on 2025-04-03 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0005_recipe_author_recipe_created_on_recipe_updated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recipe_images/')),
                ('description', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ledger.recipe')),
            ],
        ),
    ]
