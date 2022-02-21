from django.contrib import admin
from diet_app.models import Ingredient, IngredientRecipe, Recipe, RecipeMealPlan, Cuisine, MealPlan

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(IngredientRecipe)
admin.site.register(Recipe)
admin.site.register(RecipeMealPlan)
admin.site.register(Cuisine)
admin.site.register(MealPlan)