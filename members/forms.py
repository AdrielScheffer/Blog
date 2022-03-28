import email
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from posts.models import UserProfile

class Sign_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email','password1', 'password2')

    
    def __init__(self, *args, **kwargs):
        super(Sign_form, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


#class login_form() i have to use bootstrap on the login form too





class Edit_profile_settings(UserChangeForm):

    class Meta:
        model = User
        fields = ["username","first_name","last_name", "email", ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
        }



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model=User
        fields=('old_password','new_password1 ','new_password2')
        


class create_profile_form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('bio','profile_pic','instagram_url', 'twitter_url','facebook_url')

        widgets={
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic': forms.FileInput(attrs={ 'class': 'form-control'}),
            'instagram_url': forms.TextInput( attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput( attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput( attrs={'class': 'form-control'}),
        }




class Edit_profile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('bio','profile_pic','instagram_url', 'twitter_url','facebook_url')

        widgets={
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic': forms.FileInput(attrs={ 'class': 'form-control'}),
            'instagram_url': forms.TextInput( attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput( attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput( attrs={'class': 'form-control'}),
        }
