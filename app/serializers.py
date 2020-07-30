from app.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)


    class Meta:
        model = Post
        fields = ['title','status','content','updated','publication_date']

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name','posts']