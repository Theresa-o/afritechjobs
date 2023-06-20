from rest_framework import serializers

from afritechjobsapi.models import JobLevel


class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = ['id', 'job_level_choices']


class PostAJobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = ['id']