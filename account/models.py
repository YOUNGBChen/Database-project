from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.username

