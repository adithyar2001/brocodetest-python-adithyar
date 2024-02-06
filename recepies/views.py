from django.shortcuts import render,redirect
from .models import Recipe
from .forms import RecipeForm

def createrecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe')
    else:
        form = RecipeForm()
    return render(request, 'createrecipe.html', {'form': form})

def recipe(request):
    recipes= Recipe.objects.all()
    return render(request,"recipes.html",{'recipes':recipes})