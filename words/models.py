from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Card(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse('cards_detail', kwargs={'pk': self.id})


class Category(models.Model):
    name = models.CharField(max_length=100)
    gradelevel = models.IntegerField()
    cards = models.ManyToManyField(Card)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'category_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for card_id: {self.card_id} @{self.url}"

      


