from django.shortcuts import render
from core.models import ProjectComplete

# Create your views here.
def home(request):
    project_complete = ProjectComplete.objects.all()
    context = {
        'project':project_complete,
        'title':'Home'
    }
    return render(request,'home.html',context)


