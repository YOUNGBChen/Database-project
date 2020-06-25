from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    idcard = models.CharField(max_length=30, null=True)
    borrowed = models.IntegerField(max_length=5, null=True)
    staff = models.IntegerField(max_length=2, null=True)
    deposit = models.IntegerField(max_length=5, null=True)
    def __str__(self):
        return self.username

