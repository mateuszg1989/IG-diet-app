import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient

from diet_app.models import Ingredient, Recipe, Cuisine, MealPlan, RecipeMealPlan, IngredientRecipe


@pytest.fixture
def ingredients():
    lst = []
    a = Ingredient.objects.create(name='kokos', nutrient=1, glycemic_index=1)
    lst.append(a)
    b = Ingredient.objects.create(name='ananas', nutrient=2, glycemic_index=2)
    lst.append(b)
    c = Ingredient.objects.create(name='cytryna', nutrient=3, glycemic_index=3)
    lst.append(c)
    return lst




@pytest.fixture
def mealplans():
    lst = []
    a = MealPlan.objects.create(name='wtorkowy', amount=5)
    lst.append(a)
    b = MealPlan.objects.create(name='sobotni', amount=4)
    lst.append(b)
    c = MealPlan.objects.create(name='niedzielny', amount=6)
    lst.append(c)
    return lst

@pytest.fixture
def recipes():
    lst = []
    a = Recipe.objects.create(title='zupka', cooking_time=30, difficulty_level=1, description='szybka zupka',)
    lst.append(a)
    b = Recipe.objects.create(title='tosty', cooking_time=25, difficulty_level=3, description='szybkie tosty',)
    lst.append(b)
    c = Recipe.objects.create(title='kanapki', cooking_time=37, difficulty_level=2, description='szybkie kanapki',)
    lst.append(c)
    return lst


@pytest.fixture
def cuisines():
    lst = []
    a = Cuisine.objects.create(name='kuchnia gruzinska')
    lst.append(a)
    b = Cuisine.objects.create(name='kuchnia amerykanska')
    lst.append(b)
    c = Cuisine.objects.create(name='kuchnia niemiecka')
    lst.append(c)
    return lst


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


@pytest.fixture
def example_mealplan():
    mp = MealPlan.objects.create(name='mp1', amount=5)
    return mp


@pytest.fixture
def example_ingredient_recipe(example_recipe, example_ingredient):
    ingrec = IngredientRecipe.objects.create(ingredient='ingred', recipe='reci', grammage=20)
    return ingrec


@pytest.fixture
def new_user():
    x = User(username='mateusz')
    x.set_password('gawrys')
    x.save()
    return x