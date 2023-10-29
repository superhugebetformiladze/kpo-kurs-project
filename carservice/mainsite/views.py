from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import *
from .forms import ServiceRequestForm
from random import sample
from django.urls import reverse
from telegram import Bot
import asyncio
from datetime import datetime


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

def index(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save()
            
            # Отправка сообщения в Telegram
            chat_id = settings.TELEGRAM_CHAT_ID
            formatted_timestamp = service_request.timestamp.strftime('%H:%M, %d-%m-%Y')
        

            message_text = f"Новая заявка!\n\n" \
                           f"Имя: {service_request.name}\n" \
                           f"Марка автомобиля: {service_request.car_brand}\n" \
                           f"Модель автомобиля: {service_request.car_model}\n" \
                           f"Услуга: {service_request.service_name}\n" \
                           f"Номер телефона: {service_request.phone_number}\n" \
                           f"Время отправки: {formatted_timestamp}"
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(bot.send_message(chat_id, message_text))
                     
            return redirect('index')
    else:
        form = ServiceRequestForm()

    services = Service.objects.all()
    random_services = sample(list(services), 3)
    service_request_url = reverse('service_request_submission')

    return render(request, 'mainsite/index.html', {'services': random_services, 'form': form, 'service_request_url': service_request_url})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    services = Service.objects.all()
    random_services = sample(list(services.exclude(pk=service_id)), 3)
    return render(request, 'mainsite/service_detail.html', {'service': service, 'services': random_services})

def services(request):
    services = Service.objects.all()
    return render(request, 'mainsite/services.html', {'services': services})
