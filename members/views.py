from cProfile import Profile
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
from .forms import  Sign_form, PasswordChangingForm,create_profile_form,Edit_profile_settings,Edit_profile
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from posts.models import UserProfile

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class=  Sign_form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class=  Edit_profile_settings
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



class PasswordChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'
    def get_context_data(self, *args, **kwargs):
        
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        page_user= get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    

class EditProfileView(generic.UpdateView):
    model = UserProfile
    form_class = Edit_profile
    #fields = ['bio', 'profile_pic','instagram_url', 'twitter_url', 'facebook_url']
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')


class CreateProfilePage(CreateView):
    
    model = UserProfile
    form_class = create_profile_form
    template_name= 'registration/create_profile.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProfilePage, self).form_valid(form)