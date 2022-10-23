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
    path('categories/<int:category_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cards/', views.CardList.as_view(), name='cards_index'),
    path('cards/<int:pk>/', views.CardDetail.as_view(), name='cards_detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete', views.CardDelete.as_view(), name='cards_delete'),
    path('categories/<int:category_id>/assoc_card/<int:card_id>/', views.assoc_card, name='assoc_card'),
]