# Generated by Django 3.0.7 on 2020-06-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
