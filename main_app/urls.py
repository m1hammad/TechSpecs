from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('tech/', views.tech_index, name = 'index'),
    path('tech/<int:tech_id>', views.tech_detail, name='detail')
]
