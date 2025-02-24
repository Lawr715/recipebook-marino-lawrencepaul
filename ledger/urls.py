from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.recipe_list, name='recipe-list'),
    path('recipe/1/', views.recipe_1, name='recipe-1'),
    path('recipe/2/', views.recipe_2, name='recipe-2'),
]