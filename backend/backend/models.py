from django.db import models
from django.contrib.auth.models import User

class image(models.Model):
    name = models.CharField(max_length=50)
    Main_img = models.ImageField(upload_to='images/')