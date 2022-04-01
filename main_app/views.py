from django.shortcuts import render, redirect
from main_app.models import Tech, Customize
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from main_app.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class TechCreate(LoginRequiredMixin, CreateView):
    model = Tech
    fields = ['name', 'processor', 'display', 'ram', 'storage', 'os', 'price', 'image']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TechUpdate(LoginRequiredMixin, UpdateView):
    model = Tech
    fields = ['name', 'processor', 'display', 'ram', 'storage', 'os', 'price']

class TechDelete(LoginRequiredMixin, DeleteView):
    model = Tech
    success_url = '/tech/'

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

@login_required
def tech_index(request):
    laptops = Tech.objects.filter(user=request.user)
    return render(request, 'tech/index.html', {'laptops': laptops})

@login_required
def tech_detail(request, tech_id):
    laptop = Tech.objects.get(id=tech_id)
    unapplied_customizations = Customize.objects.exclude(id__in = laptop.customizations.all().values_list('id'))
    review_form = ReviewForm()
    return render(request, 'tech/detail.html', {'laptop': laptop, 'review_form': review_form, 'customizations': unapplied_customizations})

@login_required
def add_review(request, tech_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.tech_id = tech_id
        new_review.save()
    return redirect('detail', tech_id=tech_id)

class CustomizeList(LoginRequiredMixin, ListView):
    model = Customize
    
class CustomizeDetail(LoginRequiredMixin, DetailView):
    model = Customize
    
class CustomizeCreate(LoginRequiredMixin, CreateView):
    model = Customize
    fields = '__all__'

class CustomizeUpdate(LoginRequiredMixin, UpdateView):
    model = Customize
    fields = '__all__'

class CustomizeDelete(LoginRequiredMixin, DeleteView):
    model = Customize
    success_url = '/customize/'
  
@login_required  
def assoc_customize(request, tech_id, customize_id):
    Tech.objects.get(id=tech_id).customizations.add(customize_id)
    return redirect('detail', tech_id=tech_id)

@login_required
def disassoc_customize(request, tech_id, customize_id):
    Tech.objects.get(id=tech_id).customizations.remove(customize_id)
    return redirect('detail', tech_id=tech_id)


def signup(request):
    error_message=''
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
