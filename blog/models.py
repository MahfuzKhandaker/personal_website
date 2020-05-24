from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from blog.utils import get_read_time
from django.utils.safestring import mark_safe

from markdown_deux import markdown

# from django.contrib.auth import get_user_model
# User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True,unique=True)

    objects = models.Manager()

    def __str__(self): 
        return self.name


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    main_image      = models.ImageField(upload_to='images/', blank=True)
    title           = models.CharField(max_length=255)
    slug            = models.SlugField(null=False, unique=True)
    body            = models.TextField()
    created_on      = models.DateTimeField(auto_now_add=True)
    status          = models.IntegerField(choices=STATUS, default=0)
    last_modified   = models.DateTimeField(auto_now=True)
    categories      = models.ManyToManyField('Category', related_name='posts')
    read_time       = models.IntegerField(default=0)
    number_of_views = models.IntegerField(default=0, null=True, blank=True) 
    number_of_likes = models.IntegerField(default=0, null=True, blank=True) 

    objects = models.Manager()

    class Meta: 
        ordering = ['-created_on']
 
    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    # def get_markdown(self):
    #     content = self.body
    #     return markdown(content)


    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.body:
        html_string = instance.body
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var
pre_save.connect(pre_save_post_receiver, sender=Post)
        

class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')
    parent          = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    content         = models.TextField()
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.user.email)

    def get_absolute_url(self):
        return reverse('comment_thread', args=[self.pk])
    
    def get_delete_url(self):
        return reverse('comment_delete', args=[self.pk])
        
    def children(self): #replies
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
