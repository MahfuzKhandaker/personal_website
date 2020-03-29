from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from accounts.forms import UserCreationForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth import settings

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class LoginView(auth_views.LoginView):
    success_url = reverse_lazy('home')
    template_name = 'login.html'


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)