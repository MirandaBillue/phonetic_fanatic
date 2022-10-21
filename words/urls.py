from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories_index, name='index'),
    path('categories/<int:category_id>/', views.categories_detail, name='detail'),
]