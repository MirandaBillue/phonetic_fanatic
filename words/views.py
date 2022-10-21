from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class CategoryCreate(CreateView):
    model = Category
    fields = ['name', 'gradelevel']    
    success_url = '/categories/'

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'gradelevel']    

class CategoryDelete(DeleteView):
    model = Category  
    success_url = '/categories/'