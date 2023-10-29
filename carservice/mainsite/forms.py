from django import forms
from .models import ServiceRequest, Service

class ServiceRequestForm(forms.ModelForm):

    service_name = forms.ModelChoiceField(queryset=Service.objects.all(), label='Выберите услугу')

    class Meta:
        model = ServiceRequest
        fields = ['name', 'car_brand', 'car_model', 'service_name', 'phone_number']
        labels = {
            'name': 'Ваше имя', 
            'car_brand': 'Марка автомобиля', 
            'car_model': 'Модель автомобиля', 
            'phone_number': 'Номер телефона',
        }
