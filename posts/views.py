from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, CreateView, ListView, UpdateView
from .models import Post, Category
from django.urls import reverse_lazy
from .forms import PostForm, UpdateForm
# Create your views here.


class Home(ListView):
    model= Post
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
class Post_detail(DetailView):
    model = Post
    template_name = 'post_detail.html'

    
class Update_post(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    

class Delete_post(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class Create_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(Create_post, self).form_valid(form)


def CategoryView(request, cats):
    category_post= Post.objects.filter(category=cats.replace('-',' '))


    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_post':category_post})



def Category_list(request):
    cat_menu_list = Category.objects.all()


    return render(request, 'categories_list.html', {'cat_menu_list':cat_menu_list})