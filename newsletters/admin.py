from django.contrib import admin
from .models import NewsUsers, Newsletter

class NewslettersAdmin(admin.ModelAdmin):
    list_display =('email','date_added',)

admin.site.register(NewsUsers, NewslettersAdmin)

admin.site.register(Newsletter)