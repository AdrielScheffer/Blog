
from django.db import models
from django.forms import CharField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255,default='sin titulo')
    header_image = models.ImageField(blank=True, null =True, upload_to =".media/images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE,null = True)
    date_create = models.DateTimeField(auto_now_add=True)
    body = RichTextField()
    category = models.CharField(max_length=255, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    snippet= models.CharField(max_length=255)



    def __str__(self):

        return self.title 

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        
        #return reverse('post_detail', args =(str(self.id)))
        return reverse('home')


    



class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null =True, upload_to ="profile-images/")
    instagram_url = models.CharField(max_length=255, blank=True, null =True)
    twitter_url = models.CharField(max_length=255, blank=True, null =True)
    facebook_url = models.CharField(max_length=255, blank=True, null =True)


    def __str__(self):

        return str(self.user)

    def get_absolute_url(self):
        
        
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = RichTextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return "%s- %s" % (self.post.title, self.body)