
from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import Tech


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def tech_index(request):
    laptops = Tech.objects.all()
    return render(request, 'tech/index.html', {'laptops': laptops})

def tech_detail(request, tech_id):
    laptop = Tech.objects.get(id=tech_id)
    return render(request, 'tech/detail.html', {'laptop': laptop})