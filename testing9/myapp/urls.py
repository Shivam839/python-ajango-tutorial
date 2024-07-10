from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('blog/', views.blog,name='blog'),
    path('contact/', views.contact,name='contact'),
    path('services/', views.services,name='services'),
    path('product/', views.product,name='product'),
    path('about/', views.about,name='blog'),
    

]
