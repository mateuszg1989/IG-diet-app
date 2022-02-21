"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from diet_app.views import MainPageView, RecipesListView, RecipeDetailsView, RecipeAddView, MenuView, RecipeDeleteView, RecipeUpdateView
from diet_app.views import LoginView, LogoutView, AddUserView, CuisineListView, CuisineDetailsView, MealPlanAddView
from diet_app.views import MealPlanListView, MealPlanDetailsView, AddIngredientToRecipe, AddRecipeToMealPlanV2
from diet_app.views import IngredientsListView, IngredientDetailsView, IngredientAddView, IngredientUpdateView, IngredientDeleteView
from diet_app.views import MealPlanDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', MenuView.as_view(), name='menu'),
    path('', MainPageView.as_view()),
    path('recipe_list/', RecipesListView.as_view(), name='recipe-list'),
    path('cuisine_list/', CuisineListView.as_view(), name='cuisine-list'),
    path('ingredients_list/', IngredientsListView.as_view()),
    path('mealplan_list/', MealPlanListView.as_view()),
    path('cuisine_details/<int:id>/', CuisineDetailsView.as_view()),
    path('ingredient_details/<int:id>/', IngredientDetailsView.as_view()),
    path('mealplan_details/<int:id>/', MealPlanDetailsView.as_view()),
    path('recipe/<int:id>/', RecipeDetailsView.as_view()),
    path('add_recipe/', RecipeAddView.as_view()),
    path('update_recipe/<int:pk>/', RecipeUpdateView.as_view(), name='update-recipe'),
    path('delete_recipe/<int:pk>/', RecipeDeleteView.as_view(), name='delete-recipe'),
    path('add_mealplan/', MealPlanAddView.as_view()),
    path('add_ingredient/', IngredientAddView.as_view()),
    path('update_ingredient/<int:pk>/', IngredientUpdateView.as_view(), name='update-ingredient'),
    path('delete_ingredient/<int:pk>/', IngredientDeleteView.as_view(), name='delete-ingredient'),
    path('delete_mealplan/<int:pk>/', MealPlanDeleteView.as_view(), name='delete-mealplan'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('add_user/', AddUserView.as_view()),
    path('add_ingrecipe/<int:id>', AddIngredientToRecipe.as_view(), name='add-ingredient-recipe'),
    path('add_recipemealplan/<int:id>/', AddRecipeToMealPlanV2.as_view(), name='add-recipemealplan'),
]