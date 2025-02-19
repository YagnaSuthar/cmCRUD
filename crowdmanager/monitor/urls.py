from . import views
from django.urls import path,include

urlpatterns = [
  path('<int:pk>/', views.monitorHome, name='monitorHome'),

]
