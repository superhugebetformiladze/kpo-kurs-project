from django.db import models
from django.urls import reverse

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    additional_info = models.TextField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'service_id': self.pk})
    
class ServiceRequest(models.Model):
    name = models.CharField(max_length=255)
    car_brand = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name