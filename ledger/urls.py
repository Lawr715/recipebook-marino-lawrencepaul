from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path("recipes/list/", views.recipe_list, name="recipe-list"),
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe-detail"),
    path("ingredients/<int:pk>/", views.ingredient_detail, name="ingredient-detail"),
]