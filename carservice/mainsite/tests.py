from django.test import TestCase
from django.urls import reverse
from .models import Service
from django.core.files.uploadedfile import SimpleUploadedFile

class IndexPageTest(TestCase):
    def setUp(self):
        image1 = SimpleUploadedFile("service1.jpg", content=b'', content_type="image/jpg")
        image2 = SimpleUploadedFile("service2.jpg", content=b'', content_type="image/jpg")
        image3 = SimpleUploadedFile("service3.jpg", content=b'', content_type="image/jpg")
        image4 = SimpleUploadedFile("service4.jpg", content=b'', content_type="image/jpg")
        # Создайте тестовые данные
        self.service1 = Service.objects.create(name="Service 1", description="Description 1", price=10.0, image=image1)
        self.service2 = Service.objects.create(name="Service 2", description="Description 2", price=20.0, image=image2)
        self.service3 = Service.objects.create(name="Service 3", description="Description 3", price=30.0, image=image3)
        self.service4 = Service.objects.create(name="Service 4", description="Description 4", price=40.0, image=image4)


    def test_index_page_status_code(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)

    def test_index_page_contains_service_data(self):
        response = self.client.get(reverse('services'))

        # Проверьте, что данные из тестовых объектов Service отображаются на странице
        self.assertContains(response, self.service1.name)
        self.assertContains(response, self.service1.description)
        self.assertContains(response, self.service1.image)

        self.assertContains(response, self.service2.name)
        self.assertContains(response, self.service2.description)
        
        self.assertContains(response, self.service3.name)
        self.assertContains(response, self.service3.description)

        self.assertContains(response, self.service4.name)
        self.assertContains(response, self.service4.description)
