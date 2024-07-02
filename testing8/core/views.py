from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contactUs(request):
    return render(request, 'contactUs.html')
def Blog(request):
    return render(request, "Blog.html")
def FAQs(request):
    return render(request, 'FAQs.html')
def Product(request):
    return render(request, 'Product.html')
def services(request):
    return render(request, 'services.html')
