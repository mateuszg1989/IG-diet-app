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
def test_cuisine_details_view(client, cuisine):
    url = reverse('cuisine-details', kwargs={'id': cuisine.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_recipe_details_view(client, example_recipe):
    url = reverse('recipe-details', kwargs={'id': example_recipe.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_mealplan_details_view(client, example_mealplan):
    url = reverse('mealplan-details', kwargs={'id': example_mealplan.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_ingredient_details_view(client, example_ingredient):
    url = reverse('ingredient-details', kwargs={'id': example_ingredient.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_ingredient(client):
    url = reverse('add-ingredient')
    response = client.get(url)
    assert response.status_code == 302



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
def test_add_meal_plan(client, user):
    client.force_login(user)
    dct = {
        'name': 'meal plan 3',
        'amount': 5
    }
    url = reverse('add-mealplan')
    response = client.post(url, dct)
    assert response.status_code == 302
    assert MealPlan.objects.get(**dct)


@pytest.mark.django_db
def test_add_meaplan2(client):
    url = reverse('add-mealplan')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_recipe(client, example_recipe):
    dct = {
        'title': 'przepis',
        'cooking_time': 10,
        'difficulty_level': 2,
        'description': 'bla, bla, bla'
    }
    url = reverse('add-recipe')
    response = client.post(url, dct)
    assert response.status_code == 302
    assert Recipe.objects.get(**dct)




@pytest.mark.django_db
def test_add_recipe2(client):
    url = reverse('add-recipe')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_list_ingredients(client):
    url = reverse('ingredients-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_ingredients2(client, three_ingredients):
    response = client.get('/ingredients_list/')
    assert response.context['ingredients'][0].name == 'Ananas'
    assert response.context['ingredients'][1].name == 'Cytryna'
    assert response.context['ingredients'][2].name == 'Kokos'


@pytest.mark.django_db
def test_list_mealplans(client):
    url = reverse('mealplan-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_mealplans2(client, three_mealplans):
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
def test_cuisine_list2(client):
    url = reverse('cuisine-list')
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


@pytest.mark.django_db
def test_add_ingrec(client, example_ingredient, example_recipe):
    dct = {
        'ingredient': example_ingredient.id,
        'grammage': 20
    }
    url = reverse('add-ingredient-recipe', kwargs={'id': example_recipe.id})
    response = client.post(url, dct)
    assert response.status_code == 302
    assert IngredientRecipe.objects.get(**dct)


@pytest.mark.django_db
def test_add_ingrec2(client, example_recipe):
    url = reverse('add-ingredient-recipe', kwargs={'id': example_recipe.id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_recipe_mealplan(client, example_recipe, example_mealplan, user):
    client.force_login(user)
    dct = {
        'recipe': example_recipe.id,
        'meal': 3
    }
    url = reverse('add-recipemealplan', kwargs={'id': example_mealplan.id})
    response = client.post(url, dct)
    assert response.status_code == 302
    assert RecipeMealPlan.objects.get(**dct)


@pytest.mark.django_db
def test_add_recipe_mealplan2(client, example_mealplan):
    url = reverse('add-recipemealplan', kwargs={'id': example_mealplan.id})
    response = client.get(url)
    assert response.status_code == 302

# @pytest.mark.django_db
# def test_ingredient_update_view(client, example_ingredient):
#     url = reverse('update-ingredient', kwargs={'id': example_ingredient.id})
#     response = client.get(url)
#     assert Ingredient.objects.save(
#         name='cos',
#         nutrient=2,
#         glycemic_index=2
#     )

@pytest.mark.django_db
def test_login_view(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view2(client, new_user):
    dct= {
        'login':'mateusz',
        'password':'gawrys'
    }
    url = reverse('login')
    response = client.post(url, dct)
    assert response.wsgi_request.user.is_authenticated

