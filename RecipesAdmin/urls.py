from django.contrib import admin
from django.urls import path, include
from Recipes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Recipes.urls')),
]