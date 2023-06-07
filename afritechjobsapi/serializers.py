from rest_framework import serializers
from .models import Blog, Event, WorkResources, HiringGuide, Category, Profile, JobSkills, PostAJob, JobLocations, JobType, JobLevel

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

class HiringGuideSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    # slug = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )
    category = CategorySerializer(many=True, read_only=True)
    #put back image and slug field after updating the model and deleting previous content from admin
    class Meta:
        model = HiringGuide
        fields = ['id', 'title', 'content', 'category', 'author', 'meta_description', 'date_created', 'date_updated', 'post_status']

class JobSkillsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = JobSkills
        fields = ['id', 'title', 'category']

class JobLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocations
        fields = ['id', 'name']

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id', 'job_type_choices']

class JobLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLevel
        fields = ['id', 'job_level_choices']

class PostAJobSerializer(serializers.ModelSerializer):
    job_category = CategorySerializer(many=True)
    job_skills = JobSkillsSerializer(many=True)
    job_type = JobTypeSerializer()
    job_location = JobLocationsSerializer(many=True)
    job_level = JobLevelSerializer(many=True)
    created_by = ProfileSerializer(read_only=True)

    class Meta:
        model = PostAJob
        fields = ['id', 'job_title', 'job_category', 'job_skills', 'job_salary_range', 'job_description', 'job_type', 'job_location', 'job_level', 'job_application_link',  'company_name', 'company_hq', 'company_logo', 'companys_website', 'company_contact_email', 'company_description', 'date_created', 'date_updated', 'created_by']
