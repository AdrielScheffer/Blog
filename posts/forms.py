
from django import forms
from .models import Post,Category,Comment
from django.forms import ModelForm, Textarea
from posts.models import Post
from PIL import Image
from django.core.files.storage import default_storage as storage



choices= Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)



class PostForm(forms.ModelForm):
    required_css_class = 'required-field'
    class Meta:
        model = Post
        fields = ('title','category','header_image', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={ 'class': 'form-control'}),
            'body': forms.Textarea( attrs={'class': 'form-control'}),
            'snippet': forms.Textarea( attrs={'class': 'form-control'}),
        }         


        

class UpdateForm(forms.ModelForm):
    required_css_class = 'required-field'
    class Meta:
        model = Post
        fields = ('title', 'body', 'header_image','snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs= {"class": "form-control"}),
            'snippet': forms.Textarea( attrs={'class': 'form-control'}),
        }           
  





class CommentForm(forms.ModelForm):
    required_css_class = 'required-field'
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea( attrs= {"class": "form-control"}),
            
        }           
  