from django.shortcuts import render
from blog.models import Post
from django.views import generic

class Home(generic.ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['post_num'] = Post.objects.count()
        return context