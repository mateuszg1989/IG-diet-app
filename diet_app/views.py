from django.shortcuts import render, redirect
from django.views import View
from diet_app.models import Recipe, Ingredient, MealPlan, Cuisine
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from diet_app.forms import LoginForm, RegisterForm, RecipeAddForm, AddIngredientToRecipeModelForm, \
    AddRecipeToMealPlanModelFormV2, SearchForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class MainPageView(View):

    def get(self, request):
        return render(request, 'diet_app/index.html')


class MenuView(View):
    def get(self, request):
        return render(request, 'diet_app/menu.html')


class RecipesListView(View):
    def get(self, request):
        recipes = Recipe.objects.all().order_by('title')
        return render(request, 'diet_app/recipes_list.html', {'recipes': recipes})


class MealPlanListView(View):
    def get(self, request):
        mealplans = MealPlan.objects.all().order_by('name')
        return render(request, 'diet_app/mealplans_list.html', {'mealplans': mealplans})


class MealPlanDetailsView(View):
    def get(self, request, id):
        mealplan = MealPlan.objects.get(id=id)
        recipes = mealplan.recipe_set.all()
        return render(request, 'diet_app/mealplan_details.html', {'mealplan': mealplan, 'recipes': recipes})


class CuisineListView(View):
    def get(self, request):
        cuisines = Cuisine.objects.all().order_by('name')
        return render(request, 'diet_app/cuisine_list.html', {'cuisines': cuisines})


class CuisineDetailsView(View):
    def get(self, request, id):
        cuisine = Cuisine.objects.get(id=id)
        recipes = cuisine.recipe_set.all()
        return render(request, 'diet_app/cuisine_details.html', {'cuisine': cuisine, 'recipes': recipes})


class IngredientsListView(View):
    def get(self, request):
        ingredients = Ingredient.objects.all().order_by('name')
        return render(request, 'diet_app/ingredients_list.html', {'ingredients': ingredients})


class IngredientDetailsView(View):
    def get(self, request, id):
        ingredient = Ingredient.objects.get(id=id)
        return render(request, 'diet_app/ingredient_details.html', {'ingredient': ingredient})


class IngredientAddView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = '/ingredients_list'


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/ingredients_list'


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredients_list'


class RecipeDetailsView(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        ingredients = recipe.ingredient.all()
        return render(request, 'diet_app/recipe_details.html', {'recipe': recipe, 'ingredients': ingredients})


class RecipeAddView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeAddForm
    success_url = '/recipe_list'


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'cooking_time', 'difficulty_level', 'description', 'cuisine']
    template_name_suffix = '_update_form'
    success_url = '/recipe_list'


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipe_list'


class MealPlanAddView(LoginRequiredMixin, CreateView):
    model = MealPlan
    fields = '__all__'
    success_url = '/mealplan_list'


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    success_url = '/mealplan_list'


class AddRecipeToMealPlanV2(LoginRequiredMixin, View):
    def get(self, request, id):
        meal_plan = MealPlan.objects.get(id=id)
        form = AddRecipeToMealPlanModelFormV2(meal_plan)
        return render(request, 'diet_app/add_recipe_to_mealplan.html', {'form': form})

    def post(self, request, id):
        meal_plan = MealPlan.objects.get(id=id)
        form = AddRecipeToMealPlanModelFormV2(meal_plan, request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.meal_plan = meal_plan
            new_recipe.save()
            return redirect(f'/mealplan_details/{id}/')
        else:
            return render(request, 'diet_app/add_recipe_to_mealplan.html', {'form': form})


class AddIngredientToRecipe(View):
    def get(self, request, id):
        form = AddIngredientToRecipeModelForm()
        recipe = Recipe.objects.get(id=id)
        return render(request, 'diet_app/ingredientrecipe_form.html', {'form': form})

    def post(self, request, id):
        form = AddIngredientToRecipeModelForm(request.POST)
        recipe = Recipe.objects.get(id=id)
        if form.is_valid():
            new_ingredient = form.save(commit=False)
            new_ingredient.recipe = recipe
            new_ingredient.save()
            return redirect(f'/recipe/{id}/')
        else:
            return render(request, 'diet_app/ingredientrecipe_form.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'diet_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['login']
            user_password = form.cleaned_data['password']
            user = authenticate(username=user_login, password=user_password)
            if user is None:
                return render(request, 'diet_app/login.html', {'form': form})
            else:
                login(request, user)
                return redirect('/menu/')
        else:
            return render(request, 'diet_app/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'diet_app/add_user.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['username']
            user_password = form.cleaned_data['pass1']
            user_first_name = form.cleaned_data['first_name']
            user_last_name = form.cleaned_data['last_name']
            user_email = form.cleaned_data['email']
            User.objects.create_user(
                username=user_login,
                password=user_password,
                first_name=user_first_name,
                last_name=user_last_name,
                email=user_email
            )
            return redirect('/login')
        else:
            return render(request, 'diet_app/add_user.html', {'form': form})


class SearchView(View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'diet_app/search.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            recipes = Recipe.objects.filter(title__icontains=form.cleaned_data['query'])
            return render(
                request,
                'diet_app/search.html',
                {'form': form, 'recipes': recipes}
            )
        else:
            return render(request, 'diet_app/search.html', {'form': form})