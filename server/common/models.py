from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15, default='')
    email = models.TextField(default='')
    password = models.CharField(max_length=20, default='')
    token = models.TextField(default='')

    class Meta:
        ordering = ['id']


class Posting(models.Model):
    nickname = models.CharField(max_length=15, default='')
    content = models.CharField(max_length=10000, default='')
    sentiment = models.TextField(default='')
    image = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    token = models.TextField(default='')

    class Meta:
        ordering = ['nickname']