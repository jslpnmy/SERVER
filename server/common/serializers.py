from rest_framework import serializers
from .models import Profile, Posting


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'nickname', 'email', 'password', 'token']


class PostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Posting
        fields = ['nickname', 'token', 'content', 'image']