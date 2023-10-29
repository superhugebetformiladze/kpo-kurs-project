from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'car_brand', 'car_model', 'service_name', 'phone_number']
        labels = {
            'name': 'Ваше имя', 
            'car_brand': 'Марка автомобиля', 
            'car_model': 'Модель автомобиля', 
            'service_name': 'Название услуги', 
            'phone_number': 'Номер телефона',
        }
