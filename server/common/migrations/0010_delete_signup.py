# Generated by Django 3.2.7 on 2021-10-04 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_rename_signlogin_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]