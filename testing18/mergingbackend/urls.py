from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service')
]
