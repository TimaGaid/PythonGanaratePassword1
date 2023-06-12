from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    thepassword = 'testing'

    characters = list('abcdefghijklmnoprstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDIFGHIJKLMNOPRSTUVWXYZ')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    if request.GET.get('numbers'):
        characters.extend('0123456789')

    lenght = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'password.html', {'password': thepassword})
