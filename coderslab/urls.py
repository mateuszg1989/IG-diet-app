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
from diet_app.views import MainPageView, RecipesListView, RecipeDetailsView, RecipeAddView, MenuView, RecipeDeleteView,\
    RecipeUpdateView
from diet_app.views import LoginView, LogoutView, AddUserView, CuisineListView, CuisineDetailsView, MealPlanAddView
from diet_app.views import MealPlanListView, MealPlanDetailsView, AddIngredientToRecipe, AddRecipeToMealPlanV2
from diet_app.views import IngredientsListView, IngredientDetailsView, IngredientAddView, IngredientUpdateView,\
    IngredientDeleteView
from diet_app.views import MealPlanDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', MenuView.as_view(), name='menu'),
    path('', MainPageView.as_view(), name='main'),
    path('recipe_list/', RecipesListView.as_view(), name='recipe-list'),
    path('cuisine_list/', CuisineListView.as_view(), name='cuisine-list'),
    path('ingredients_list/', IngredientsListView.as_view(), name='ingredients-list'),
    path('mealplan_list/', MealPlanListView.as_view(), name='mealplan-list'),
    path('cuisine_details/<int:id>/', CuisineDetailsView.as_view(), name='cuisine-details'),
    path('ingredient_details/<int:id>/', IngredientDetailsView.as_view(), name='ingredient-details'),
    path('mealplan_details/<int:id>/', MealPlanDetailsView.as_view(), name='mealplan-details'),
    path('recipe/<int:id>/', RecipeDetailsView.as_view(), name='recipe-details'),
    path('add_recipe/', RecipeAddView.as_view(), name='add-recipe'),
    path('update_recipe/<int:pk>/', RecipeUpdateView.as_view(), name='update-recipe'),
    path('delete_recipe/<int:pk>/', RecipeDeleteView.as_view(), name='delete-recipe'),
    path('add_mealplan/', MealPlanAddView.as_view(), name='add-mealplan'),
    path('add_ingredient/', IngredientAddView.as_view(), name='add-ingredient'),
    path('update_ingredient/<int:pk>/', IngredientUpdateView.as_view(), name='update-ingredient'),
    path('delete_ingredient/<int:pk>/', IngredientDeleteView.as_view(), name='delete-ingredient'),
    path('delete_mealplan/<int:pk>/', MealPlanDeleteView.as_view(), name='delete-mealplan'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_user/', AddUserView.as_view(), name='add-user'),
    path('add_ingrecipe/<int:id>', AddIngredientToRecipe.as_view(), name='add-ingredient-recipe'),
    path('add_recipemealplan/<int:id>/', AddRecipeToMealPlanV2.as_view(), name='add-recipemealplan'),
]
