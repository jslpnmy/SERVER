# Generated by Django 3.2.7 on 2021-10-10 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=15)),
                ('content', models.CharField(default='', max_length=10000)),
                ('sentiment', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d/')),
                ('token', models.TextField(default='')),
            ],
            options={
                'ordering': ['nickname'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=15)),
                ('email', models.TextField(default='')),
                ('password', models.CharField(default='', max_length=20)),
                ('token', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
