import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from urllib.parse import quote_plus
from . import models


# Create your views here.
def home(request):
    return render(request,'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    stuff_for_frontend={

        'search':search,

    }
    return render(request,'my_app/new_search.html', stuff_for_frontend)