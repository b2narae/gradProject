from django.shortcuts import render
from .models import Car

def crawling_list(request):
    cars = Car.objects.all()
    return render(request, 'crawling/crawling_list.html', {'cars': cars})

# Create your views here.
