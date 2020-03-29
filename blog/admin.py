from django.contrib import admin
from .models import Post, Category, Comment
# from pagedown.widgets import AdminPagedownWidget
from blog.forms import PostForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    form = PostForm
    fields = ['title', 'slug', 'body', 'main_image', 'categories',]
    
    
class CategoryAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)