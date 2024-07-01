from django.urls import path
from . import views
urlpatterns=[
    path("",views.home, name='home' ),
    path("aboutUs/",views.aboutUs, name='aboutUs' ),
    path("contact/",views.contact, name='contact' ),
    path("login/",views.login, name='login' ),
    path("signup/",views.signup, name='signup' ),
    path("cart/",views.cart, name='cart' ),
    path("blog/",views.blog, name='blog' )
]