from django.urls import path
from . import views

app_name = "ledger"

urlpatterns = [
    path("list/", views.recipe_list, name="recipe-list"),
    path("<int:recipe_id>/", views.recipe_detail, name="recipe-detail"),
]