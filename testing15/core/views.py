from django.shortcuts import render
from .models import Records

# Create your views here.
def home(request):
    records = Records.objects.all()
    context = {
        "Records":records,
        "title":'Project_X - Home'
    }
    return render(request,'home.html',context)

def dashboard(request):
    records = Records.objects.all()
    context = {
        "Records":records,
        "title":'Project_X - dashboard'
    }
    return render(request,'dashboard.html',context)

def signOut(request):
    records = Records.objects.all()
    context = {
        "Records":records,
        "title":'Project_X - signOut'
    }
    return render(request,'signOut.html',context)
