import pytest

from django.urls import reverse

from diet_app.models import Ingredient, Recipe, MealPlan, RecipeMealPlan, IngredientRecipe


def test_main(client):
    url = reverse('main')
    response = client.get(url)
    assert response.status_code == 200


def test_menu(client):
    url = reverse('menu')
    response = client.get(url)
    assert response.status_code == 200



@pytest.mark.django_db
def test_add_ingredient2(client, user):
    client.force_login(user)
    response = client.post('/add_ingredient/', {
        'name': 'groszek',
        'nutrient': '1',
        'glycemic_index': '1'
    })
    assert response.status_code == 302
    assert Ingredient.objects.get(
        name='groszek',
        nutrient=1,
        glycemic_index=1
    )


@pytest.mark.django_db
def test_add_meal_plan(client):
    dct = {
        'name': 'meal plan 3',
        'amount': 5
    }
    url = reverse('add-mealplan')
    response = client.post(url, dct)
    assert response.status_code == 302


@pytest.mark.django_db
def test_list_ingredients(client, three_ingredients):
    response = client.get('/ingredients_list/')
    assert response.context['ingredients'][0].name == 'Ananas'
    assert response.context['ingredients'][1].name == 'Cytryna'
    assert response.context['ingredients'][2].name == 'Kokos'


@pytest.mark.django_db
def test_list_mealplans(client, three_mealplans):
    response = client.get('/mealplan_list/')
    assert response.context['mealplans'][0].name == 'niedzielny'
    assert response.context['mealplans'][1].name == 'sobotni'
    assert response.context['mealplans'][2].name == 'wtorkowy'


@pytest.mark.django_db
def test_recipe_list(client):
    url = reverse('recipe-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_recipes(client, three_recipes):
    response = client.get('/recipe_list/')
    assert response.context['recipes'][0].title == 'kanapki'
    assert response.context['recipes'][1].title == 'tosty'
    assert response.context['recipes'][2].title == 'zupka'


@pytest.mark.django_db
def test_list_cuisines(client, three_cuisines):
    response = client.get('/cuisine_list/')
    assert response.context['cuisines'][0].name == 'kuchnia amerykanska'
    assert response.context['cuisines'][1].name == 'kuchnia gruzinska'
    assert response.context['cuisines'][2].name == 'kuchnia niemiecka'


@pytest.mark.django_db
def test_cuisine_details_view(client, cuisine):
    url = reverse('cuisine-details', kwargs={'id': cuisine.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ingredient_view(client, example_ingredient):
    url = reverse('ingredient-details', kwargs={'id': example_ingredient.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_view(client):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_user_view(client):
    url = reverse('add-user')
    response = client.get(url)
    assert response.status_code == 200

