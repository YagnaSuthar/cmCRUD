from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.eventsHome,name='eventsHome'),
   path('event/<int:pk>/',views.event,name='event'),
   path('createForm/',views.createForm,name='create-form'),
   path('delete/<int:pk>/',views.eventDelete,name='delete-event'),
   path('update/<int:pk>/',views.updateEvent,name='update-event'),
   path('monitor/<int:pk>/',include('monitor.urls')),

   
]
