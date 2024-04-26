from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    document = models.ImageField(upload_to='uploads')