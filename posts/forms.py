
from importlib.metadata import requires
from django import forms
from .models import Post,Category

choices=Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    required_css_class = 'required-field'
    class Meta:
        model = Post
        fields = ('title','category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices= choice_list, attrs={ 'class': 'form-control'}),
            'body': forms.Textarea( attrs= {"class": "form-control"}),
        }           
  

class UpdateForm(forms.ModelForm):
    required_css_class = 'required-field'
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea( attrs= {"class": "form-control"}),
        }           
  