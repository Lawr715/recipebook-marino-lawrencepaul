from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeImageForm, RecipeIngredientFormSet
from django.forms import modelform_factory

RecipeForm = modelform_factory(Recipe, fields=["name"])

@login_required
def recipe_list(request):
    """Fetch all recipes from the database and display them (only for logged-in users)."""
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, pk):
    """Fetch a specific recipe using its PK and display its ingredients and author (only for logged-in users)."""
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    images = RecipeImage.objects.filter(recipe=recipe)
    return render(request, "ledger/recipe_detail.html", {
        "recipe": recipe,
        "ingredients": ingredients,
        "images": images,
        "author": recipe.author
    })

@login_required
def add_image(request, pk):
    """Allows users to upload a new image for a specific recipe."""
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect("ledger:recipe-detail", pk=recipe.pk)
    else:
        form = RecipeImageForm()

    return render(request, "ledger/add_image.html", {"form": form, "recipe": recipe})

@login_required
def add_recipe(request):
    """Allows users to create a new recipe with ingredients."""
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        formset = RecipeIngredientFormSet(request.POST)

        if recipe_form.is_valid() and formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            formset.instance = recipe
            formset.save()
            return redirect("ledger:recipe-detail", pk=recipe.pk)
    else:
        recipe_form = RecipeForm()
        formset = RecipeIngredientFormSet()

    return render(request, "ledger/add_recipe.html", {
        "recipe_form": recipe_form,
        "formset": formset
    })