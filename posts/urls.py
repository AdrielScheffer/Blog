
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .views import Home, Create_post,Post_detail, Update_post,Delete_post


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('add_post/', Create_post.as_view(), name = 'new_post'),
    path('post/<int:pk>', Post_detail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', Update_post.as_view(), name = 'update'),
    path('post/<int:pk>/remove', Delete_post.as_view(), name = 'delete')

]