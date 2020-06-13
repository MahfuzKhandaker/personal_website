from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
from django.shortcuts import render
from .forms import NewsUserForm, NewsletterCreationForm
from . models import NewsUsers, Newsletter


def newsletter_subscribe(request):
    form = NewsUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsUsers.objects.filter(email=instance.email).exists():
            messages.warning(request,
                        "your Email Already exists in our database",
                        "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request,
                            "Your email has been submitted to the database",
                            "alert alert-success alert-dismissible")

            subject = "Thank You For Joining Our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]

            with open(settings.BASE_DIR + "/newsletters/templates/subscribe_email.txt") as f:
                newsletter_message = f.read()
            
            message = EmailMultiAlternatives(subject=subject, body=newsletter_message, from_email=from_email, to=to_email)
            html_template = get_template("subscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        'form': form
    }
    template = "subscribe.html"
    return render(request, template, context)

def newsletter_unsubscribe(request):
    form = NewsUserForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsUsers.objects.filter(email=instance.email).exists():
            NewsUsers.objects.filter(email=instance.email).delete()
            messages.success(request,
                            "Your email has been removed",
                            "alert alert-success alert-dismissible")

            subject = "You have been unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/newsletters/templates/unsubscribe_email.txt") as f:
                newsletter_message = f.read()
            
            message = EmailMultiAlternatives(subject=subject, body=newsletter_message, from_email=from_email, to=to_email)
            html_template = get_template("unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

        else:
            messages.warning(request,
                        "Sorry we didn't find your email address",
                        "alert alert-warning alert-dismissible")
    
    context ={
        'form': form
    }
    template = 'unsubscribe.html'
    return render(request, template, context)

def newsletter_control(request):
    form = NewsletterCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id=instance.id)
        if newsletter.status == "Published":
            subject = newsletter.subject
            body    = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            for email in newsletter.email.all():
                send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
        
    context = {
        'form': form,
    }
    template = 'newsletter_control.html'
    return render(request, template, context)