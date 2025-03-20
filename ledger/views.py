from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient

@login_required
def recipe_list(request):
    """Fetch all recipes from the database and display them (only for logged-in users)."""
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, recipe_id):
    """Fetch a specific recipe using its ID and display its ingredients and author (only for logged-in users)."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)  # Keep ingredients functionality from Lab 1 & 2
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe, "ingredients": ingredients, "author": recipe.author})