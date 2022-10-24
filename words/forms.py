from django.forms import ModelForm
from .models import Card, Category, Photo

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['word']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['url']

       