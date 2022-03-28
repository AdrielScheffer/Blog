
from django.urls import path
from .views import UserRegisterView,UserEditView,PasswordChangeView, UserProfileView, EditProfileView,CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, name= 'password_success'),
    path('<int:pk>/profile', UserProfileView.as_view(), name = 'profileview' ),
    path('<int:pk>/edit_profile_page/', EditProfileView.as_view(), name = 'edit_profileview' ),
    path('create_profile_page/', CreateProfilePage.as_view(), name = 'create_profile' ),
]