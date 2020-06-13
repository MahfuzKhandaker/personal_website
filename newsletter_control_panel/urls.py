from django.urls import path
from newsletters.views import newsletter_control

urlpatterns = [
    path('newsletter/', newsletter_control, name='newsletter'),

]