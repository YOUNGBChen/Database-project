from django.db import models

# Create your models here.

class information(models.Model):
    isbn = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    publish = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    sort = models.CharField(max_length=30)
    year = models.CharField(max_length=30)

class users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)