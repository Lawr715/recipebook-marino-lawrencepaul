from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_list(request):
    """Fetch all recipes from the database and display them."""
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

def recipe_detail(request, recipe_id):
    """Fetch a specific recipe using its ID and display its ingredients."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe})