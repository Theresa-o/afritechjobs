from rest_framework import serializers

from afritechjobsapi.models import JobSkills
from afritechjobsapi.serializers.category import CategorySerializer


class JobSkillsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = JobSkills
        fields = ['id', 'title', 'category']


class PostAJobSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSkills
        fields = ['id']