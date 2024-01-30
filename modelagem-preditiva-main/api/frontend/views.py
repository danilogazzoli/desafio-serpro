from django.shortcuts import render
from django.http import HttpResponse
import pathlib


def index(request):
    #return HttpResponse(pathlib.Path().resolve())
    #/home/02639086901/Projects/desafio/02639086901/modelagem-preditiva-main/api
    #/home/02639086901/Projects/desafio/02639086901/modelagem-preditiva-main/api/frontend/templates

    return render(request, 'home.html')

