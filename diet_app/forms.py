import django.forms as forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from diet_app.models import Cuisine, DIFFICULTY_LEVELS, MealPlan, Recipe, MEALS, RecipeMealPlan, IngredientRecipe


class LoginForm(forms.Form):
    """Login details form"""
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class RecipeAddForm(forms.ModelForm):
    """New recipe add form"""
    class Meta:
        model = Recipe
        exclude = ['ingredient', 'meal_plan']


class AddIngredientToRecipeModelForm(forms.ModelForm):
    """Ingredient to recipe add form"""
    class Meta:
        model = IngredientRecipe
        exclude = ['recipe']

    # def clean(self):
    #     """function created to avoid adding the same product to recipe more than once"""
    #     amount = super().clean()
    #     count = amount['ingredient'].ingredientrecipe_set.count()
    #     if count != 0:
    #         raise ValidationError('Ten składnik został już dodany do tego przepisu!')


def validate_username_is_not_taken(value):
    """Login unique check function"""
    users = User.objects.filter(username=value)
    if len(users) > 0:
        raise ValidationError("Ten login jest już zajęty")


class RegisterForm(forms.Form):
    """User register form"""
    username = forms.CharField(label='Nazwa użytkownika', max_length=50, validators=[validate_username_is_not_taken])
    pass1 = forms.CharField(label='hasło', max_length=50, widget=forms.PasswordInput)
    pass2 = forms.CharField(label="powtórz hasło", max_length=50, widget=forms.PasswordInput)
    first_name = forms.CharField(label="imię", max_length=50)
    last_name = forms.CharField(label='nazwisko', max_length=50)
    email = forms.EmailField(label='email', max_length=50)

    def clean(self):
        """function used to check if passwords are the same"""
        cleaned_data = super().clean()
        if cleaned_data['pass1'] != cleaned_data['pass2']:
            raise ValidationError("Hasła nie są takie same!")
        return cleaned_data


class AddRecipeToMealPlanModelFormV2(forms.ModelForm):
    """Recipe to meal plan add form"""
    class Meta:
        model = RecipeMealPlan
        fields = '__all__' ##jak jest exclude = ['meal_plan] to wtedy oczywiscie nie dziala ponizsza funkcja, inne pola z modelu nie dzialaja, moze da sie jakos ukryc to pole wyboru w formularzu

    def clean(self):
        amount = super().clean()
        count = amount['meal_plan'].recipemealplan_set.count()
        if count >= 6:
            raise ValidationError('Meal plan może mieć maksymalnie 6 posiłków')