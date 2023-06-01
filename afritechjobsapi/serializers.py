from rest_framework import serializers
from .models import Blog, Event, WorkResources, Category, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'is_email_confirmed']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    slug = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'content', 'category', 'slug', 'author', 'meta_description', 'date_created', 'date_updated', 'post_status']

class EventSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        fields = ['__all__']

class WorkResourcesSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = WorkResources
        fields = ['__all__']
