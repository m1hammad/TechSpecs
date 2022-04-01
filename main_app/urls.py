from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('tech/', views.tech_index, name = 'index'),
    path('tech/<int:tech_id>', views.tech_detail, name='detail'),
    path('tech/create', views.TechCreate.as_view(), name='tech_create'),
    path('tech/<int:pk>/update', views.TechUpdate.as_view(), name='tech_update'),
    path('tech/<int:pk>/delete', views.TechDelete.as_view(), name='tech_delete'),
    path('tech/<int:tech_id>/add_review/', views.add_review, name = 'add_review'),
    
    # CRUD Operations on Customizations
    path('customize/', views.CustomizeList.as_view(), name='customize_index'),
    path('customize/<int:pk>/', views.CustomizeDetail.as_view(), name='customize_detail'),
    path('customize/create/', views.CustomizeCreate.as_view(), name='customize_create'),
    path('customize/<int:pk>/update', views.CustomizeUpdate.as_view(), name='customize_update'),
    path('customize/<int:pk>/delete', views.CustomizeDelete.as_view(), name='customize_delete'),
    
    # Associate customization with laptop
    path('tech/<int:tech_id>/assoc_customize/<int:customize_id>', views.assoc_customize, name='assoc_customize'),
    # Disassociate customization from laptop
    path('tech/<int:tech_id>/disassoc_customize/<int:customize_id>', views.disassoc_customize, name='disassoc_customize'),
    
    #signup
    path('accounts/signup', views.signup, name='signup')
]
