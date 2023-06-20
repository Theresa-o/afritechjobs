from rest_framework import serializers

from afritechjobsapi.models import PostAJob
from afritechjobsapi.serializers.category import CategorySerializer, PostAJobCategorySerializer
from afritechjobsapi.serializers.job_level import JobLevelSerializer, PostAJobLevelSerializer
from afritechjobsapi.serializers.job_location import (
    JobLocationsSerializer,
    PostAJobLocationsSerializer,
)
from afritechjobsapi.serializers.job_skills import JobSkillsSerializer, PostAJobSkillsSerializer
from afritechjobsapi.serializers.job_type import JobTypeSerializer, PostAJobTypeSerializer
from afritechjobsapi.serializers.users import PostAJobUserSerializer, UserSerializer


class JobDetailSerializer(serializers.ModelSerializer):
    job_category = CategorySerializer(read_only=True)
    job_skills = JobSkillsSerializer(many=True, read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    job_location = JobLocationsSerializer(many=True, read_only=True)
    job_level = JobLevelSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = PostAJob
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    job_category = PostAJobCategorySerializer(read_only=True)
    job_skills = PostAJobSkillsSerializer(many=True, read_only=True)
    job_type = PostAJobTypeSerializer(read_only=True)
    job_location = PostAJobLocationsSerializer(many=True, read_only=True)
    job_level = PostAJobLevelSerializer(many=True, read_only=True)
    created_by = PostAJobUserSerializer(read_only=True)

    class Meta:
        model = PostAJob
        fields = (
            'id',
            'job_title',
            'job_category',
            'job_skills',
            'job_salary_range',
            'job_description',
            'job_type',
            'job_location',
            'job_level',
            'job_application_link',
            'company_name',
            'company_hq',
            'companys_website',
            'company_contact_email',
            'company_description',
            'created_by',
        )

    def create(self, validated_data):
        request = self.context['request']

        job_category_pk = request.data.get('job_category')
        validated_data['job_category_id'] = job_category_pk

        job_type_pk = request.data.get('job_type')
        validated_data['job_type_id'] = job_type_pk

        created_by_pk = request.data.get('created_by')
        validated_data['created_by_id'] = created_by_pk

        job_skills_data = request.data.get('job_skills')
        validated_data['job_skills'] = job_skills_data

        job_location_data = request.data.get('job_location')
        validated_data['job_location'] = job_location_data

        job_level_data = request.data.get('job_level')
        validated_data['job_level'] = job_level_data

        instance = super().create(validated_data)

        return instance

    def update(self, instance, validated_data):
        request = self.context['request']

        if request.data.get('job_category'):
            job_category_pk = request.data['job_category']
            validated_data['job_category_id'] = job_category_pk

        if request.data.get('job_type'):
            job_type_pk = request.data['job_type']
            validated_data['job_type_id'] = job_type_pk

        if request.data.get('created_by'):
            created_by_pk = request.data['created_by']
            validated_data['created_by_id'] = created_by_pk

        if request.data.get('job_skills'):
            job_skills_data = request.data['job_skills']
            validated_data['job_skills'] = job_skills_data

        if request.data.get('job_location'):
            job_location_data = request.data['job_location']
            validated_data['job_location'] = job_location_data

        if request.data.get('job_level'):
            job_level_data = request.data['job_level']
            validated_data['job_level'] = job_level_data

        instance = super().update(instance, validated_data)

        return instance
