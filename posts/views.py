from django.shortcuts import render, get_object_or_404
from django.views.generic import DeleteView, DetailView, CreateView, ListView, UpdateView
from .models import Post, Category,Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm, UpdateForm, CommentForm
from django.http import HttpResponseRedirect
# Create your views here.


class Home(ListView):
    model= Post
    template_name = 'index.html'
    ordering = ['-date_create']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        
        return context

class Post_detail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Post_detail, self).get_context_data(*args, **kwargs)
        the_post = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = the_post.total_likes()

        liked=False
        if the_post.likes.filter(id = self.request.user.id).exists():
            liked = True

        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"] = liked
        return context
    
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

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked= False
    if post.likes.filter(id= request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


class AddCommentView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    """
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    """
    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.name = self.request.user
        return super().form_valid(form)
    def get_success_url(self):

        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})