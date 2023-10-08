from django.shortcuts import render
from .models import *
from random import sample
from django.shortcuts import get_object_or_404

def index(request):
    services = Service.objects.all()
    random_services = sample(list(services), 3)
    return render(request, 'mainsite/index.html', {'services': random_services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    services = Service.objects.all()
    random_services = sample(list(services.exclude(pk=service_id)), 3)
    return render(request, 'mainsite/service_detail.html', {'service': service, 'services': random_services})

def services(request):
    services = Service.objects.all()
    return render(request, 'mainsite/services.html', {'services': services})
