from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def home(request):
    context ={
        'title':"Home"
    }
    return  render(request,'index.html',context)
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        message=request.POST.get('message')

        contact = Contact(
            name=name,
            number=number,
            email =email,
            message=message
        )

        contact.save()
        return redirect('thankyou')
        
      

    context ={
        'title':"Contact Us"
    }
    return  render(request,'contact.html',context)
def about(request):
    context ={
        'title':"About Us"
    }
    return render(request,'about.html',context)
def service(request):
    context ={  
        'title':"Our Services"
    }
    return render(request,'service.html',context)

def userData(request):
    context = {
        'userdata': Contact.objects.all(),
        "title":"User Data"
    }
    return render(request,'userdata.html',context)

def thankyou(request):
    context={
        'title':"Thank You!"
    }
    return render(request,'thanku.html',context)