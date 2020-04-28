from django.urls import path
from .views import newsletter_subscribe, newsletter_unsubscribe

app_name = 'newsletters'
urlpatterns = [
path('subscribe', newsletter_subscribe, name='subscribe'),
path('unsubscribe', newsletter_unsubscribe, name='unsubscribe'),
]
