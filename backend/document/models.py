from django.db import models

from django.contrib.auth.models import User

def image_upload_to(instance, filename):
    category = instance.category if hasattr(instance, 'category') else 'default'
    return f'images/{category}/{filename}'

class Image(models.Model):
    title = models.CharField(max_length=255, default= '1')
    category = models.CharField(max_length=50, default= 'default') 
    image = models.ImageField(upload_to=image_upload_to)