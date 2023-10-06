from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('service/<str:service_name>/', views.service_detail, name='service_detail'), 
]
