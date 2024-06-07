from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('men',views.men,name='men'),
    path('women',views.women,name='women'),
    path('bag',views.bag,name='bag'),
    path('watch',views.watch,name='watch'),
    path('shoes',views.shoes,name='shoes'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('cart',views.cart,name='cart'),
]
