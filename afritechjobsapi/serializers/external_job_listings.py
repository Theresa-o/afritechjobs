from rest_framework import serializers

from afritechjobsapi.models import ExternalJobListing
from afritechjobsapi.serializers.category import CategorySerializer
from afritechjobsapi.serializers.job_level import JobLevelSerializer
from afritechjobsapi.serializers.job_location import JobLocationsSerializer
from afritechjobsapi.serializers.job_skills import JobSkillsSerializer
from afritechjobsapi.serializers.job_type import JobTypeSerializer
from afritechjobsapi.serializers.users import UserSerializer



class ExternalJobListingSerializer(serializers.ModelSerializer):
    job_category = CategorySerializer(read_only=True)
    job_skills = JobSkillsSerializer(many=True, read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    job_location = JobLocationsSerializer(many=True, read_only=True)
    job_level = JobLevelSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = ExternalJobListing
        fields = '__all__'