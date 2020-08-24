from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


# STYLE_CHOICES = ['without_images', 'default']

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # news_images = models.ForeignKey(NewsImage, related_name='images', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news_items = models.ForeignKey(NewsItem, related_name='images', on_delete=models.CASCADE, null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.photo.name



