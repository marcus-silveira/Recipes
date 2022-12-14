from django.urls import path
from Recipes.views import home, sobre, contato

urlpatterns = [
    path('home', home),
    path('sobre', sobre),
    path('contato', contato),
]