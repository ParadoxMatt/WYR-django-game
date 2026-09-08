from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("WELCOME TO WOULD YOU RATHER?. \n A GAME ABOUT EXPERIENCES. \n THIS IS GOING TO BE THE MENU PAGE")