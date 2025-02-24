from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path("list/", recipe_list, name="recipe_list"),
    path("<int:recipe_id>/", recipe_detail, name="recipe_detail"),
]
