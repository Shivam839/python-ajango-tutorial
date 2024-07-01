from django.shortcuts import render,HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("<h3>Kya be hero </h3>")

