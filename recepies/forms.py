from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name','ingredients','categories')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'enter recipe'}),
            'ingredients': forms.TextInput(attrs={'placeholder': 'enter ingredients'}),
        }