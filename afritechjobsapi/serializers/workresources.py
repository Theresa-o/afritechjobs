from rest_framework import serializers
from afritechjobsapi.models import (WorkResources)
from afritechjobsapi.serializers.category import CategorySerializer


class WorkResourcesSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = WorkResources
        # put back image and slug field after updating the model and deleting previous content from admin
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
