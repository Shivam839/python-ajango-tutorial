from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('Services',views.services,name='Services'),
    path('SignOut',views.signout,name='SignOut'),

]
