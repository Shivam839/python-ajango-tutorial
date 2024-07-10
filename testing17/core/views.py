from django.shortcuts import render
from .models import Records, Contact

# Create your views here.

def home(request):
    studentData = Records.objects.all()
    context = {
        'title':'Home',
        'Students':studentData
    }
    return render(request,'home.html',context)
def about(request):
    context = {
        'title':'About'
    }
    return render(request,'about.html',context)

def contact(request):
      
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        message=request.POST.get('message')

        new_contact = Contact(
            name=name,
            email=email,
            phoneNumber=phonenumber,
            message=message,
        )
        new_contact.save()

    context = {
        'title':'Contact',
       
        
    }
    return render(request,'contact.html',context)


