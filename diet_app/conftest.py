import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient

from diet_app.models import Ingredient, Recipe, Cuisine

