from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile

class RecipeIngredientInline(admin.TabularInline):
    """ Allows inline editing of Recipe Ingredients within a Recipe """
    model = RecipeIngredient
    extra = 1

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Admin customization for Ingredient model """
    search_fields = ["name"]

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """ Admin customization for Recipe model """
    list_display = ["name", "author", "created_on", "updated_on"]  # Added author, created_on, updated_on
    search_fields = ["name", "author__username"]
    inlines = [RecipeIngredientInline]
    list_filter = ["author", "created_on"]

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    """ Admin customization for RecipeIngredient model """
    list_display = ["recipe", "ingredient", "quantity"]
    list_filter = ["recipe"]
    search_fields = ["ingredient__name", "recipe__name"]

class ProfileInline(admin.StackedInline):
    """ Allows inline editing of Profile in User Admin """
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    """ Extends UserAdmin to show Profile inline """
    inlines = [ProfileInline]

# Unregister default User model and register it with Profile inline
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register Profile separately for direct access in Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Admin customization for Profile model """
    list_display = ["user", "name"]
    search_fields = ["user__username", "name"]