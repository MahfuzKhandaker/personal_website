from django.shortcuts import render
from .models import About

# Create your views here.
def about_view(request):
    instance = About.objects.all()
    context = {
        'instance': instance
    }
    return render(request, 'about.html', context)