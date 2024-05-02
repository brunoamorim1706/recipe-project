from django.shortcuts import render

# Create your views here.
def home(resquest):
    return render(resquest, 'recipes/pages/home.html', context={
        'name': 'Bruno Amorim',
    })


def recipe(resquest, id):
    return render(resquest, 'recipes/pages/recipe-view.html', context={
        'name': 'Bruno Amorim',
    })