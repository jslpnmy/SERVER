from django.db import models


class Profile(models.Model):
    nickname = models.CharField(max_length=15, default='')
    email = models.TextField(default='')
    password = models.CharField(max_length=20, default='')
    token = models.TextField(default='')

    class Meta:
        ordering = ['id']


class Posting(models.Model):
    nickname = models.CharField(max_length=15, default='')
    token = models.TextField(default='')
    content = models.CharField(max_length=10000, default='')
    image = models.ImageField(upload_to='common', null=True)

    class Meta:
        ordering = ['nickname']