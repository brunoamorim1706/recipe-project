from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(resquest):
    return HttpResponse('Home')


def sobre(resquest):
    return HttpResponse('Sobre')


def contato(resquest):
    return HttpResponse('Contato')