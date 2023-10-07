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