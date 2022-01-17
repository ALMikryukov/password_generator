from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html',{'password': 'hui43g6LoO3b8'})


def about(request):
    return render(request, 'generator/about.html',{'password': 'hui43g6LoO3b8'})


def password(request):     
    characters =list('qwertyuioassdfghjklzxcvbnm')

    if request.GET.get('upercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    
    if request.GET.get('speatial'):
        characters.extend(list("'!@#$%^&*()_+{[]<>/?*/-+`~'"))

    if request.GET.get('numbers'):
        characters.extend(list("1234567890"))

    lenght = int(request.GET.get('lenght',12))
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
     
    return render(request, 'generator/password.html',{'password': thepassword})