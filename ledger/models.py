from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:ingredient-detail", args=[self.pk])  # ✅ Sets absolute URL

class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe-detail", args=[self.pk])  # ✅ Sets absolute URL

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")  # ✅ related_name for Ingredient
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")  # ✅ related_name for Recipe

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"