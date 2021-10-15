from django.db import models

# Create your models here.
class File(models.Model):
    """File model"""
    username = models.CharField(max_length = 50)
    filename = models.CharField(max_length = 100)
    docfile = models.FileField(upload_to='documents/', default='')
