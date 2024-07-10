from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('aboutUs/',views.aboutUs,name='aboutUs'),
    path('products',views.products,name='products'),
    path('services/',views.services,name='services'),
]