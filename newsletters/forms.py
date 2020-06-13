from django import forms
from pagedown.widgets import PagedownWidget
from .models import NewsUsers, Newsletter

class NewsUserForm(forms.ModelForm):
    class Meta:
        model = NewsUsers
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

class NewsletterCreationForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Newsletter
        fields = ['subject', 'body', 'email', 'status']
    