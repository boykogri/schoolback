from news.models import NewsItem, NewsImage
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'photo']


class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True)

    class Meta:
        model = NewsItem
        fields = ['id', 'title', 'text', 'images']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
