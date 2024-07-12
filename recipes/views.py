from django.shortcuts import get_list_or_404, render
from recipes.models import Recipe



def home(resquest):
    recipes = get_list_or_404(Recipe.objects.filter(is_published=True).order_by('-id'))
    return render(resquest, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(resquest, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))

    

    return render(resquest, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'tilte': f'{recipes[0].category.name} - Category |',
    })


def recipe(resquest, id):
    recipe = Recipe.objects.filter(pk=id, is_published=True).first()

    return render(resquest, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })