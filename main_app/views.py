from django.shortcuts import render, redirect
from main_app.models import Tech, Customize
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from main_app.forms import ReviewForm

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
    unapplied_customizations = Customize.objects.exclude(id__in = laptop.customizations.all().values_list('id'))
    review_form = ReviewForm()
    return render(request, 'tech/detail.html', {'laptop': laptop, 'review_form': review_form, 'customizations': unapplied_customizations})

def add_review(request, tech_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.tech_id = tech_id
        new_review.save()
    return redirect('detail', tech_id=tech_id)

class CustomizeList(ListView):
    model = Customize
    
class CustomizeDetail(DetailView):
    model = Customize
    
class CustomizeCreate(CreateView):
    model = Customize
    fields = '__all__'

class CustomizeUpdate(UpdateView):
    model = Customize
    fields = '__all__'

class CustomizeDelete(DeleteView):
    model = Customize
    success_url = '/customize/'
    
def assoc_customize(request, tech_id, customize_id):
    Tech.objects.get(id=tech_id).customizations.add(customize_id)
    return redirect('detail', tech_id=tech_id)

def disassoc_customize(request, tech_id, customize_id):
    Tech.objects.get(id=tech_id).customizations.remove(customize_id)
    return redirect('detail', tech_id=tech_id)
