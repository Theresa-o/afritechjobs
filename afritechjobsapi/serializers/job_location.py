from rest_framework import serializers

from afritechjobsapi.models import JobLocations


class JobLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocations
        fields = ['id', 'name']


class PostAJobLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocations
        fields = ['id']