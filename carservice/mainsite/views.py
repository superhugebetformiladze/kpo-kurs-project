from django.shortcuts import render
from .models import *

def index(request):
    services = Service.objects.all()
    return render(request, 'mainsite/index.html', {'services': services})

def service_detail(request, service_id):
    return render(request, 'mainsite/service_detail.html', {'service_id': service_id})
