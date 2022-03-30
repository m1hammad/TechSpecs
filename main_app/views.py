from django.shortcuts import render, redirect
from main_app.models import Tech
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
    review_form = ReviewForm()
    return render(request, 'tech/detail.html', {'laptop': laptop, 'review_form': review_form})

def add_review(request, tech_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.tech_id = tech_id
        new_review.save()
    return redirect('detail', tech_id=tech_id)