from django.db import models

class NewsUsers(models.Model):
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "NewsUser"
        verbose_name_plural = "NewsUsers"

    def __str__(self):
        return self.email
        
    objects = models.Manager()


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    subject = models.CharField(max_length=250)
    body    = models.TextField()
    email   = models.ManyToManyField(NewsUsers)
    status  = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()

    def __str__(self):
        return self.subject