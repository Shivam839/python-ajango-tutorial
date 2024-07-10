from django.shortcuts import render
from .models import Recipes

# Create your views here.

def home(request):
    recipelist = Recipes.objects.all()
    context = {
        'title':'Recipes - Home',
        'recipies': recipelist
    }
    return render(request,'home.html' , context)
def services(request):
    context = {
        'title':'Recipes - Services'
    }
    return render(request,'services.html' , context)
def signout(request):
    context = {
        'title':'Recipes - signout'
    }
    return render(request,'signout.html' , context)