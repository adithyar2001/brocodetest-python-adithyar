from django.urls import path
from .import views
urlpatterns = [
    path('',views.createrecipe,name="createrecipe"),
    path('recipe/',views.recipe,name="recipe"),
]
