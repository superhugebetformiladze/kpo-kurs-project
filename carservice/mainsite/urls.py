from django.urls import path
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('service/<int:service_id>/', service_detail, name='service_detail'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
