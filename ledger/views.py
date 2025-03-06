from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeIngredient, Ingredient 

def recipe_list(request):
    """ Fetch all recipes from the database and display them """
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

def recipe_detail(request, recipe_id):
    """ Fetch a specific recipe using its ID and display its ingredients """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(request, "ledger/recipe_detail.html", {"recipe": recipe, "ingredients": ingredients})

def ingredient_detail(request, pk):
    """ Fetch a specific ingredient using its ID and display its details """
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, "ledger/ingredient_detail.html", {"ingredient": ingredient})