from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200, default='')
    slug = models.CharField(max_length = 200)
    body = models.TextField()
    pub_date = models.DateTimeField(default = timezone.now)
    
    def __unicode__(self):
        return self.title

class Meta:
    ordering = ('-pub_date')

class Contact(models.Model):
    title = models.CharField(max_length = 200, default='')
    name = models.CharField(max_length = 200)
    tel = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.title
