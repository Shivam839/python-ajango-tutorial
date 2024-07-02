from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('contactUs/',views.contactUs, name='contact US' ),
    path('about/',views.about, name='about' ),
    path('Blog/',views.Blog, name='Blog' ),
    path('FAQs/',views.FAQs, name='Faqs' ),
    path('Product/',views.Product, name='product' ),
    path('services/',views.services, name='services' ),
]