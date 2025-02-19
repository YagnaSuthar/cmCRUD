from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.baseHome,name='baseHome'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.register,name="register"),
    path('contact/',views.contact,name='contactus'),

]
