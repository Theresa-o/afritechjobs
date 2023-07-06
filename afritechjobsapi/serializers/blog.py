from rest_framework import serializers
from afritechjobsapi.models import (Blog)
from afritechjobsapi.serializers.category import CategorySerializer

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    # slug = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )
    category = CategorySerializer(many=True, read_only=True)

    # put back image and slug field after updating the model and deleting previous content from admin
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'category',
            'author',
            'meta_description',
            'date_created',
            'date_updated',
            'post_status',
        ]