
from django.shortcuts import render
from django.urls import path
from .views import Home, Create_post,Post_detail, Update_post,Delete_post, CategoryView,Category_list,likeView,AddCommentView


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('add_post/', Create_post.as_view(), name = 'new_post'),
    path('post/<int:pk>', Post_detail.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', Update_post.as_view(), name = 'update'),
    path('post/<int:pk>/remove', Delete_post.as_view(), name = 'delete'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', Category_list, name='category-list'),
    path('like/<int:pk>', likeView, name='like'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name = 'add_comment')
]