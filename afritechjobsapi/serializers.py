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
    # slug = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )
    category = CategorySerializer(many=True, read_only=True)
    #put back image and slug field after updating the model and deleting previous content from admin
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'category', 'author', 'meta_description', 'date_created', 'date_updated', 'post_status']

class EventSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
         #put back banner image field after updating the model and deleting previous content from admin
        fields = ['id', 'event_name', 'event_details', 'author', 'event_host', 'event_date', 'registration_fees', 'date_created', 'date_updated', 'is_attending']

class WorkResourcesSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = WorkResources
            #put back image and slug field after updating the model and deleting previous content from admin
        fields = ['id', 'title', 'content', 'category', 'author', 'meta_description', 'date_created', 'date_updated', 'post_status']
