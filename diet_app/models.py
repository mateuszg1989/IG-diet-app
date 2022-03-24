from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

DIFFICULTY_LEVELS = (
    (1, 'bardzo prosty'),
    (2, 'prosty'),
    (3, 'średniozaawansowany'),
    (4, 'zaawansowany'),
    (5, 'trudny')
)

GLYCEMIC_INDEX = (
    (1, 'IG<55'),
    (2, 'IG 56-69'),
    (3, 'IG>70')
)

NUTRIENTS = (
    (1, 'białko'),
    (2, 'tłuszcz'),
    (3, 'węglowodan'),
    (4, 'woda'),
    (5, 'inne')
)

MEALS = (
    (1, 'Śniadanie'),
    (2, 'Drugie śniadanie'),
    (3, 'Obiad'),
    (4, 'Podwieczorek'),
    (5, 'Kolacja'),
    (6, 'Przekąska')
)


class Ingredient(models.Model):
    """Description of single ingredient, including it's glycemic index."""
    name = models.CharField(max_length=50, unique=True)
    nutrient = models.IntegerField(choices=NUTRIENTS)
    glycemic_index = models.IntegerField(choices=GLYCEMIC_INDEX)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Instructions how to prepare a single dish."""
    title = models.CharField(max_length=50)
    cooking_time = models.IntegerField(help_text='w minutach', validators=[MinValueValidator(1), MaxValueValidator(5000)])
    difficulty_level = models.IntegerField(choices=DIFFICULTY_LEVELS, default=1)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    cuisine = models.ForeignKey('Cuisine', on_delete=models.CASCADE, null=True)
    ingredient = models.ManyToManyField(Ingredient, through='IngredientRecipe')
    meal_plan = models.ManyToManyField('MealPlan', through='RecipeMealPlan')

    def __str__(self):
        return self.title


class IngredientRecipe(models.Model):
    """Many-to-many relationship model between Ingredient and Recipe."""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    grammage = models.IntegerField(help_text='w gramach', validators=[MinValueValidator(1), MaxValueValidator(5000)])

    def __str__(self):
        return str(self.ingredient)  # dodana konwersja na str po TypeError


class RecipeMealPlan(models.Model):
    """Many-to-many relationship model between Recipe and MealPlan"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    meal_plan = models.ForeignKey('MealPlan', on_delete=models.CASCADE)
    meal = models.IntegerField(choices=MEALS)

    def __str__(self):
        return str(self.recipe)


class MealPlan(models.Model):
    """Meal plan for specific day. Limitation: min. 1, max. 6 dishes per mealplan."""
    name = models.CharField(max_length=50)
    amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])

    def __str__(self):
        return self.name


class Cuisine(models.Model):
    """Type of cuisine of the recipe."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
