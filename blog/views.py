from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from blog.models import Post, Comment
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.contrib.contenttypes.models import ContentType
from blog.forms import PostForm, CommentForm
from blog.utils import get_read_time
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required


def blog_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, slug):
    instance = get_object_or_404(Post, slug=slug)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        if not request.user.is_authenticated:
            return redirect('login')
        content_type = instance.get_content_type
        object_id = instance.id
        content_data = form.cleaned_data['content']
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
    
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()
    
        Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=object_id,
            content=content_data,
            parent=parent_obj
        )
        form = CommentForm()

       
    # comments = Comment.objects.filter_by_instance(instance)
    comments = instance.comments
    context = {
        'instance': instance,
        'comments': comments,
        'comment_form': form,
        }
    return render(request, 'blog_detail.html', context)


@login_required
def comment_delete(request, pk):
    try:
        obj = Comment.objects.get(pk=pk)
    except:
        raise Http404

    if obj.user != request.user:
        response = HttpResponse("You do not have permission to delete this comment.")
        response.status_code = 403
        return response
    
    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        messages.success(request, "This has been deleted.")
        return HttpResponseRedirect(parent_obj_url)
    
    context = {
        "object": obj
    }
    return render(request, "confirm_delete.html", context)

def comment_thread(request, pk):
    obj = get_object_or_404(Comment, pk=pk)
    
    form = CommentForm(request.POST or None)
    if form.is_valid():
        if not request.user.is_authenticated:
            return redirect('login')
        content_type = obj.content_object.get_content_type
        object_id = obj.content_object.id
        content_data = form.cleaned_data['content']
        parent_obj = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
            
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()
        
        Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=object_id,
            content=content_data,
            parent=parent_obj
        )
        form = CommentForm()
       
    context = {
        'comment': obj,
        'form': form
    }
    return render(request, 'comment_thread.html', context)
