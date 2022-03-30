from django.shortcuts import render, redirect
from main_app.models import Tech
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class TechCreate(CreateView):
    model = Tech
    fields = '__all__'

class TechUpdate(UpdateView):
    model = Tech
    fields = ['name', 'processor', 'display', 'ram', 'storage', 'os', 'price']

class TechDelete(DeleteView):
    model = Tech
    success_url = '/tech/'

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