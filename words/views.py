from urllib import response
from django.shortcuts import render, redirect
from PyDictionary import PyDictionary
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Category, Photo, Card
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'words11-11'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def word(request):
   # search = request.GET.get('search')
    #dictionary = PyDictionary()
    #try:
        #if search:
            #meanings = dictionary.meaning(search)
            #synonyms = dictionary.synonym(search)
            #antonyms = dictionary.antonym(search)
       
        return render(request, 'word.html') 
        #{'search': search, 'meanings': meanings, 'synonyms': synonyms, 'antonyms': antonyms })
    #except TypeError:
        #return render(request, 'home.html', {'search': search })


@login_required
def categories_index(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'categories/index.html', { 'categories': categories })

@login_required
def categories_detail(request, category_id):
    category = Category.objects.get(id=category_id)   
    cards_category_doesnt_have = Category.objects.exclude(id__in = category.cards.all().values_list('id'))

    return render(request, 'categories/detail.html', { 
        'category': category, 'cards': cards_category_doesnt_have  })  

@login_required
def assoc_card(request, category_id, card_id):
    Category.objects.get(id=category_id).cards.add(card_id)
    return redirect('detail', category_id=category_id)

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
    fields = ('name', 'gradelevel')    

class CategoryDelete(DeleteView):
    model = Category  
    success_url = '/categories/'

class CardCreate(CreateView):
    model = Card  
    fields = ['word']

class CardUpdate(UpdateView):
    model = Card
    fields = ['word'] 

class CardDelete(DeleteView):
    model = Card 
    success_url = '/cards/'

class CardDetail(DetailView):
    model = Card
    template_name = 'cards/detail.html'

class CardList(ListView):
    model = Card
    template_name = 'cards/index.html'  

@login_required
def add_photo(request, card_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, card_id=card_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('cards_detail', pk=card_id)    


 