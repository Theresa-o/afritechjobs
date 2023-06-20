from rest_framework import serializers

from afritechjobsapi.models import JobType


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id', 'job_type_choices']


class PostAJobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id']