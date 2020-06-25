from django.db import models

# Create your models here.

class book(models.Model):
    id = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    writer = models.CharField(max_length=30, null=True)
    publish = models.CharField(max_length=30, null=True)
    sort = models.CharField(max_length=30, null=True)
    year = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.id