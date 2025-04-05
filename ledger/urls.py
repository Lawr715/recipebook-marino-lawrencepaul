from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path("list/", views.recipe_list, name="recipe-list"),
    path("<int:pk>/", views.recipe_detail, name="recipe-detail"),
    path("<int:pk>/add_image/", views.add_image, name="add-image"),
    path("add/", views.add_recipe, name="add-recipe"),
]