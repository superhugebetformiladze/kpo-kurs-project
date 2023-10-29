import os

from django.test import TestCase
from django.urls import reverse
from .models import Service, ServiceRequest
from .forms import ServiceRequestForm
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch, call
from django.conf import settings


class MainSiteTestCase(TestCase):
    def setUp(self):
        image1 = SimpleUploadedFile("service1.jpg", content=b'', content_type="image/jpg")
        image2 = SimpleUploadedFile("service2.jpg", content=b'', content_type="image/jpg")
        image3 = SimpleUploadedFile("service3.jpg", content=b'', content_type="image/jpg")

        self.service1 = Service.objects.create(name="Тестовое имя 1", description="Тестовое описание 1", additional_info="Доп инфо 1", price=10.0, image=image1)
        self.service2 = Service.objects.create(name="Тестовое имя 2", description="Тестовое описание 2", additional_info="Доп инфо 2", price=20.0, image=image2)
        self.service3 = Service.objects.create(name="Тестовое имя 3", description="Тестовое описание 3", additional_info="Доп инфо 3", price=30.0, image=image3)

        self.service_request = ServiceRequest.objects.create(name="Иван Иванов", car_brand="Toyota", car_model="Camry", service_name=self.service1, phone_number="89091112299")

    def tearDown(self):
        # Удаление тестовых файлов после завершения тестов
        for service in Service.objects.all():
            if service.image:
                file_path = service.image.path

                # Проверка, существует ли файл по данному пути
                if os.path.exists(file_path):
                    os.remove(file_path)


    def test_index_page_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_contains_service_data(self):
        services = Service.objects.all()
        response = self.client.get(reverse('index'))

        for service in services:
            self.assertContains(response, service.name)
            self.assertContains(response, service.description)
            self.assertContains(response, service.image)

    @patch('mainsite.views.Bot.send_message')
    def test_send_telegram_message(self, mock_send_message):
            
        form_data = {
            'name': self.service_request.name,
            'car_brand': self.service_request.car_brand,
            'car_model': self.service_request.car_model,
            'service_name': self.service_request.service_name.pk,
            'phone_number': self.service_request.phone_number,
        }
        form = ServiceRequestForm(data=form_data)
        print(form.errors)
        
        # Проверяем, что форма валидна
        self.assertTrue(form.is_valid())
        
        # Отправляем форму
        response = self.client.post(reverse('index'), data=form_data)
        
        self.assertEqual(response.status_code, 302)  # 302 - перенаправление

        formatted_timestamp = self.service_request.timestamp.strftime('%H:%M, %d-%m-%Y')
        chat_id=settings.TELEGRAM_CHAT_ID

        mock_send_message.assert_called_once_with(
            chat_id,
            'Новая заявка!\n\n'
            f'Имя: {self.service_request.name}\n'
            f'Марка автомобиля: {self.service_request.car_brand}\n'
            f'Модель автомобиля: {self.service_request.car_model}\n'
            f'Услуга: {self.service_request.service_name}\n'
            f'Номер телефона: {self.service_request.phone_number}\n'
            f'Время отправки: {formatted_timestamp}',
        )

    def test_services_page_status_code(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)

    def test_services_page_contains_service_data(self):
        services = Service.objects.all()
        response = self.client.get(reverse('services'))

        for service in services:
            self.assertContains(response, service.name)
            self.assertContains(response, service.description)
            self.assertContains(response, service.image)

    def test_service_page_status_code(self):
        services = Service.objects.all()

        for service in services:
            response = self.client.get(reverse('service_detail', args=[service.id]))
            self.assertEqual(response.status_code, 200)

    def test_service_page_contains_service_data(self):
        services = Service.objects.all()

        for service in services:
            response = self.client.get(reverse('service_detail', args=[service.id]))

            self.assertContains(response, service.name)
            self.assertContains(response, service.description)
            self.assertContains(response, service.image)