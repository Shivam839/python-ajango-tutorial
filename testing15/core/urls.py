from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('dashboard',views.dashboard,name='Dashboard'),
    path('signOut',views.signOut,name='SignOut')
]