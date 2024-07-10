from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'title':'Home'}
    return render(request,'index.html',context)
def about(request):
    context = {'title':'About'}
    return render(request,'about.html',context)
def contactus(request):
    context = {'title':'ContactUs'}
    return render(request,'contactus.html',context)
def privacy(request):
    context = {'title':'PrivacyPolicy'}
    return render(request,'privacy.html',context)
