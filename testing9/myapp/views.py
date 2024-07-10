from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contactpage.html')
def about(request):
    return render(request, 'aboutus.html')
def product(request):
    return render(request, 'product.html')
def services(request):
    return render(request, 'services.html')


