from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):  # ✅ Inline editing for ingredients
    model = RecipeIngredient
    extra = 1

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ["name"]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    inlines = [RecipeIngredientInline]  # ✅ Shows ingredients inside Recipe

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ["recipe", "ingredient", "quantity"]
    list_filter = ["recipe"]
    search_fields = ["ingredient__name", "recipe__name"]