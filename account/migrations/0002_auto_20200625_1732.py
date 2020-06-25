# Generated by Django 3.0.7 on 2020-06-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='borrowed',
            field=models.IntegerField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='deposit',
            field=models.IntegerField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='staff',
            field=models.IntegerField(max_length=2, null=True),
        ),
    ]