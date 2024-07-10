from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('contactus/',views.contactus,name='contact'),
    path('ourservices/',views.ourservices,name='ourservices')
]