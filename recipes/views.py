from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(resquest):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(resquest, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(resquest, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(resquest, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })


def recipe(resquest, id):
    return render(resquest, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe,
        'is_detail_page': True,
    })