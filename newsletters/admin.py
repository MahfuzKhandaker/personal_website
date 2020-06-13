from django.contrib import admin
from .models import NewsUsers, Newsletter
from newsletters.forms import NewsletterCreationForm

class NewslettersAdmin(admin.ModelAdmin):
    list_display =('subject', 'created')
    form = NewsletterCreationForm
    fields = ['subject', 'body', 'email', 'status']

admin.site.register(Newsletter, NewslettersAdmin)

admin.site.register(NewsUsers)