from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories_index, name='index'),
    path('categories/<int:category_id>/', views.categories_detail, name='detail'),
    path('categories/create/', views.CategoryCreate.as_view(), name='categories_create'),
    path('categories/<int:pk>/update', views.CategoryUpdate.as_view(), name='categories_update'),
    path('categories/<int:pk>/delete', views.CategoryDelete.as_view(), name='categories_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]