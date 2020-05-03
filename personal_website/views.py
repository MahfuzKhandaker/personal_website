from django.shortcuts import render
from blog.models import Post

def home(request):
    template = 'home.html'
    post_num = Post.objects.count()
    context = {
        'post_num': post_num
    }
    return render(request, template, context=context)