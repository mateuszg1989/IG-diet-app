import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient

from diet_app.models import Ingredient, Recipe, Cuisine, MealPlan, RecipeMealPlan



@pytest.fixture
def three_ingredients():
    Ingredient.objects.create(
        name='Kokos',
        nutrient=2,
        glycemic_index=3
    )
    Ingredient.objects.create(
        name='Ananas',
        nutrient=1,
        glycemic_index=1
    )
    Ingredient.objects.create(
        name='Cytryna',
        nutrient=3,
        glycemic_index=1
    )


@pytest.fixture
def three_mealplans():
    MealPlan.objects.create(
        name='wtorkowy',
        amount=5
    )
    MealPlan.objects.create(
        name='sobotni',
        amount=4
    )
    MealPlan.objects.create(
        name='niedzielny',
        amount=6
    )

@pytest.fixture
def three_recipes():
    Recipe.objects.create(
        title='zupka',
        cooking_time=30,
        difficulty_level=1,
        description='szybka zupka',
    )
    Recipe.objects.create(
        title='tosty',
        cooking_time=25,
        difficulty_level=3,
        description='szybkie tosty',
    )
    Recipe.objects.create(
        title='kanapki',
        cooking_time=37,
        difficulty_level=2,
        description='szybkie kanapki',
    )


@pytest.fixture
def three_cuisines():
    Cuisine.objects.create(
        name='kuchnia gruzinska'
    )
    Cuisine.objects.create(
        name='kuchnia amerykanska'
    )
    Cuisine.objects.create(
        name='kuchnia niemiecka'
    )

@pytest.fixture
def user():
    u = User.objects.create(username='mateusz', is_superuser=True)
    return u



@pytest.fixture()
def cuisine():
    cus = Cuisine.objects.create(name='moja kuchnia', )
    return cus


@pytest.fixture
def example_ingredient():
    ing = Ingredient.objects.create(name='gruszka', nutrient=1, glycemic_index=2)
    return ing


@pytest.fixture()
def example_recipe():
    rec = Recipe.objects.create(title='przepis', cooking_time=10, difficulty_level=2, description='bla, bla, bla')
    return rec