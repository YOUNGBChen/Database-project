# Generated by Django 3.0.7 on 2020-06-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ISBN', models.CharField(max_length=30, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('writer', models.CharField(max_length=30, null=True)),
                ('publish', models.CharField(max_length=30, null=True)),
                ('sort', models.CharField(max_length=30, null=True)),
                ('year', models.CharField(max_length=30, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
