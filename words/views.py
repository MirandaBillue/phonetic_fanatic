from django.shortcuts import render
from .models import Category

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def categories_index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', { 'categories': categories })


def categories_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'categories/detail.html', { 'category': category })