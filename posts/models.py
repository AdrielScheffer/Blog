from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    date_create = models.DateTimeField(auto_now_add=True)
    body = RichTextField()

    def __str__(self):

        return self.title 

    def get_absolute_url(self):
        
        return reverse('post_detail', args =(str(self.id)))