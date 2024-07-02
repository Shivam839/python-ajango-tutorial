from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home Page</h1>")


def aboutUs(request):
    return render(request, 'about.html')
    # return HttpResponse("<h1>About Us Page</h1>")

def contact(request):
    return HttpResponse("<h1>Contact Us Page</h1>")

def login(request):
    return HttpResponse("<h1>Login Page</h1>")

def signup(request):
    return HttpResponse("<h1>Sign Up Page</h1>")

def blog(request):
    return HttpResponse("<h1>Blog Page</h1>")

def cart(request):
    return HttpResponse("<h1>Cart Page</h1>")