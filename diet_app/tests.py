import pytest

from django.urls import reverse

from diet_app.models import Ingredient, Recipe, MealPlan, RecipeMealPlan, IngredientRecipe



def test_menu(client):
    url = reverse('menu')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_ingredient(client):
    dct = {
        'name': 'groszek',
        'nutrient': 1,
        'glycemic_index': 1
    }
    url = reverse('add-ingredient')
    response = client.post(url, dct)
    assert response.status_code == 302




@pytest.mark.django_db
def test_add_meal_plan(client):
    dct = {
        'name': 'meal plan 3',
        'amount': 5
    }
    url = reverse('add-mealplan')
    response = client.post(url, dct)

