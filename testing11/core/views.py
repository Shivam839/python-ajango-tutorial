from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'landingpage.html')
def contactus(request):
    return render(request, 'contactus.html')
def ourservices(request):
    return render(request,'ourservices.html')

