from rest_framework import serializers
from .models import Profile, Posting


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'nickname', 'email', 'password', 'token']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting
        fields = ['nickname', 'token', 'content', 'image']