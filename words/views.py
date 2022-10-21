from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Category, Photo
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'words11-11'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def categories_index(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'categories/index.html', { 'categories': categories })

def categories_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'categories/detail.html', { 'category': category })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)                

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'gradelevel']  

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'gradelevel']    

class CategoryDelete(DeleteView):
    model = Category  
    success_url = '/categories/'

@login_required
def add_photo(request, category_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, category_id=category_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', category_id=category_id)    