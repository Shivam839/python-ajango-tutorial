from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'title':'Home Page'}
    return render(request, 'home.html',context)
def aboutUs(request):
    context = {'title':'AboutUs Page'}
    return render(request, 'aboutUs.html',context)
def products(request):
    context = {'title':'Products Page'}
    return render(request, 'products.html',context)
def services(request):
    context = {'title':'Services Page'}
    return render(request, 'services.html',context)

