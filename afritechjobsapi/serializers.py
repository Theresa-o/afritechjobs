from rest_framework import serializers
from .models import (
    Blog,
    Event,
    WorkResources,
    HiringGuide,
    Category,
    Profile,
    JobSkills,
    PostAJob,
    JobLocations,
    JobType,
    JobLevel,
)
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


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


class EventSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        # put back banner image field after updating the model and deleting previous content from admin
        fields = [
            'id',
            'event_name',
            'event_details',
            'author',
            'event_host',
            'event_date',
            'registration_fees',
            'date_created',
            'date_updated',
            'is_attending',
        ]


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


class HiringGuideSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    # slug = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )
    category = CategorySerializer(many=True, read_only=True)

    # put back image and slug field after updating the model and deleting previous content from admin
    class Meta:
        model = HiringGuide
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


class PostAJobSerializer(serializers.Serializer):
    job_title = serializers.CharField(max_length=200)
    job_salary_range = serializers.IntegerField()
    job_description = serializers.CharField()
    job_application_link = serializers.URLField(max_length=200)
    company_name = serializers.CharField(max_length=200)
    company_hq = serializers.CharField(max_length=200)
    # company_logo = serializers.ImageField()
    companys_website = serializers.URLField(max_length=200)
    company_contact_email = serializers.EmailField(max_length=200)
    company_description = serializers.CharField()
    job_category_id = serializers.IntegerField()
    job_skills_id = serializers.ListField(child=serializers.IntegerField())
    job_type_id = serializers.IntegerField()
    job_location_id = serializers.ListField(child=serializers.IntegerField())
    job_level_id = serializers.ListField(child=serializers.IntegerField())
    created_by_id = serializers.IntegerField()
    # companylogo

    # def create(self, validated_data):

    #     return job


class JobSerializer(serializers.ModelSerializer):
    job_category = CategorySerializer(read_only=True)
    job_skills = JobSkillsSerializer(many=True, read_only=True)
    job_type = JobTypeSerializer(read_only=True)
    job_location = JobLocationsSerializer(many=True, read_only=True)
    job_level = JobLevelSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = PostAJob
        fields = '__all__'

    # def create(self, validated_data):
    #     job_category_data = validated_data.pop('job_category')
    #     job_skills_data = validated_data.pop('job_skills')
    #     job_type_data = validated_data.pop('job_type')
    #     job_location_data = validated_data.pop('job_location')
    #     job_level_data = validated_data.pop('job_level')

    # #trial 1: referenced from drf documentation
    # #returns error = IntegrityError at /jobs/create NOT NULL constraint failed: afritechjobsapi_postajob.job_category_id
    # #Create the PostAJob instance
    #     post_a_job = PostAJob.objects.create(**validated_data)

    #     # trial
    #     for level_item in job_level_data:
    #         JobLevel.objects.create(post_a_job=post_a_job, **level_item)

    #         #new trial
    #     for category_item in job_category_data:
    #         Category.objects.create(post_a_job=post_a_job, **category_item)

    #     for skills_item in job_skills_data:
    #         JobSkills.objects.create(post_a_job=post_a_job, **skills_item)

    #     JobType.objects.create(post_a_job=post_a_job, **job_type_data)

    #     # Create the related instances for job_location
    #     for location_item in job_location_data:
    #         JobLocations.objects.create(post_a_job=post_a_job, **location_item)

    #     return post_a_job

    # trial 2 from stackoverflow user help
    # error received - TypeError at /jobs/create django.db.models.query.QuerySet.create() argument after ** must be a mapping, not list
    # create the related instances for job_category
    # category = Category.objects.create(**job_category_data)
    # skills = JobSkills.objects.create(**job_skills_data)
    # location = JobLocations.objects.create(**job_location_data)
    # job_type = JobType.objects.create(**job_type_data)
    # level = JobLevel.objects.create(**job_level_data)

    # # Create the PostAJob instance
    # validated_data.update({"category": category}, {"category": category}, {"skills": skills}, {"location": location}, {"job_type": job_type}, {"level": level})
    # post_a_job = PostAJob.objects.create(**validated_data)

    # return post_a_job

    # trial 3 https://stackoverflow.com/questions/71063694/django-typeerror-get-argument-after-must-be-a-mapping-not-list
    # error 'Category' object is not subscriptable C:\Users\hp\Desktop\CS50\afritechjobsite\afritechjobsapi\views.py, line 147, in post_a_job
    #             post_a_job_serializer.save()
    #                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
    # Local vars
    # C:\Users\hp\Desktop\CS50\afritechjobsite\venv\Lib\site-packages\rest_framework\serializers.py, line 212, in save
    #             self.instance = self.create(validated_data)
    #                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
    # Local vars
    # C:\Users\hp\Desktop\CS50\afritechjobsite\afritechjobsapi\serializers.py, line 144, in create
    #             category = Category.objects.create(**category_item)[0]

    # for category_item in job_category_data:
    #     category = Category.objects.create(**category_item)[0]
    #     validated_data['job_category'] = category

    # # trial
    # for level_item in job_level_data:
    #     level = JobLevel.objects.create(**level_item)[0]
    #     validated_data['job_level'] = level

    # post_a_job = PostAJob.objects.create(**validated_data)

    # #create the related instances for job_skills
    # for skills_data in job_skills_data:
    #     skills = JobSkills.objects.create(**skills_data)
    #     post_a_job.job_skills.add(skills)

    # # Create the related instance for job_type
    # job_type = JobType.objects.create(**job_type_data)
    # post_a_job.job_type = job_type

    # # Create the related instances for job_location
    # for location_data in job_location_data:
    #     location = JobLocations.objects.create(**location_data)
    #     post_a_job.job_location.add(location)

    # # Create the related instances for job_level
    # for level_data in job_level_data:
    #     level = JobLevel.objects.create(**level_data)
    #     post_a_job.job_level.add(level)

    # return post_a_job

    # trial 4 chatgpt
    # error message 'Category' object is not iterable


#                 ret = super().data
#                    ^^^^^^^^^^^^ …
# Local vars
# C:\Users\hp\Desktop\CS50\afritechjobsite\venv\Lib\site-packages\rest_framework\serializers.py, line 253, in data
#                 self._data = self.to_representation(self.instance)
#                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
# Local vars
# C:\Users\hp\Desktop\CS50\afritechjobsite\venv\Lib\site-packages\rest_framework\serializers.py, line 522, in to_representation
#                 ret[field.field_name] = field.to_representation(attribute)
#                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ …
# Local vars
# C:\Users\hp\Desktop\CS50\afritechjobsite\venv\Lib\site-packages\rest_framework\serializers.py, line 686, in to_representation
#         return [

# Create the related instance for job_category
# if job_category_data:
#     category_data = job_category_data[0]
#     category = Category.objects.create(**category_data)
#     validated_data['job_category'] = category

# if job_level_data:
#     level_data = job_level_data[0]
#     level = JobLevel.objects.create(**level_data)
#     validated_data['job_level'] = level

# if job_type_data:
#     type_data = job_type_data[0]
#     type = JobType.objects.create(**type_data)
#     validated_data['job_type'] = type

# if job_location_data:
#     location_data = job_location_data[0]
#     location = JobLocations.objects.create(**location_data)
#     validated_data['job_location'] = location

# if job_skills_data:
#     skills_data = job_skills_data[0]
#     skills = JobSkills.objects.create(**skills_data)
#     validated_data['job_skills'] = skills


# # Create the PostAJob instance
# post_a_job = PostAJob.objects.create(**validated_data)

# return post_a_job

# trial 5 chatgpt solutionn for trials 1 errors
# error message TypeError at /jobs/ 'Category' object is not iterable HOWEVER IT CREATES THE POST AND CATEGORY but on jobs, it gives this message
# Create the related instances for job_category
# for category_item in job_category_data:
#     category = Category.objects.create(**category_item)
#     validated_data['job_category'] = category

# # Create the related instances for job_skills
# for skills_item in job_skills_data:
#     skills = JobSkills.objects.create(**skills_item)
#     validated_data['job_skills'] = skills

# # Create the related instances for job_type
# for type_item in job_type_data:
#     type = JobType.objects.create(**type_item)
#     validated_data['job_type'] = type

# # Create the related instances for job_location
# for location_item in job_location_data:
#     location = JobLocations.objects.create(**location_item)
#     validated_data['job_location'] = location

# # Create the related instances for job_level
# for level_item in job_level_data:
#     level = JobLevel.objects.create(**level_item)
#     validated_data['job_level'] = level

#         # Create the PostAJob instance
# post_a_job = PostAJob.objects.create(**validated_data)

# return post_a_job

# trial 6 chatgpt solutionn for trials 5 errors
# Create the related instances for job_category
# error message ValueError at /jobs/create Cannot assign "[<Category: Engineering>]": "PostAJob.job_category" must be a "Category" instance.
# category_items = []
# for category_item in job_category_data:
#     category = Category.objects.create(**category_item)
#     category_items.append(category)
# validated_data['job_category'] = category_items

# # Create the related instances for job_skills
# skills_items = []
# for skills_item in job_skills_data:
#     skills = JobSkills.objects.create(**skills_item)
#     skills_items.append(skills)
# validated_data['job_skills'] = skills_items

# # Create the related instances for job_type
# type_items = []
# for type_item in job_type_data:
#     job_type = JobType.objects.create(**type_item)
#     type_items.append(job_type)
# validated_data['job_type'] = type_items

# # Create the related instances for job_location
# location_items = []
# for location_item in job_location_data:
#     location = JobLocations.objects.create(**location_item)
#     location_items.append(location)
# validated_data['job_location'] = location_items

# # Create the related instances for job_level
# level_items = []
# for level_item in job_level_data:
#     level = JobLevel.objects.create(**level_item)
#     level_items.append(level)
# validated_data['job_level'] = level_items

# # Create the PostAJob instance
# post_a_job = PostAJob.objects.create(**validated_data)

# return post_a_job

# trial 7 chatgpt solutionn for trials 6 errors
# Create the related instances for job_category

# # Create the related instances for job_category
# category_items = []
# for category_item in job_category_data:
#     category = Category.objects.create(**category_item)
#     category_items.append(category)
# validated_data['job_category'] = category_items[0] if category_items else None


#     # Create the related instances for job_skills
#     for skills_item in job_skills_data:
#         skills = JobSkills.objects.create(**skills_item)
#         validated_data['job_skills'] = skills

#     # Create the related instances for job_type
#     for type_item in job_type_data:
#         type = JobType.objects.create(**type_item)
#         validated_data['job_type'] = type

#     # Create the related instances for job_location
#     for location_item in job_location_data:
#         location = JobLocations.objects.create(**location_item)
#         validated_data['job_location'] = location

#     # Create the related instances for job_level
#     for level_item in job_level_data:
#         level = JobLevel.objects.create(**level_item)
#         validated_data['job_level'] = level

#             # Create the PostAJob instance
#     post_a_job = PostAJob.objects.create(**validated_data)

#     return post_a_job


# trial 20 before he edited his comment stacover
# create the related instances for job_category
# category = Category.objects.create(**job_category_data)

# Create the PostAJob instance
# post_a_job = PostAJob.objects.create(**{**validated_data, "category": category})

# #create the related instances for job_skills
# for skills_data in job_skills_data:
#     skills = JobSkills.objects.create(**skills_data)
#     post_a_job.job_skills.add(skills)

# # Create the related instance for job_type
# job_type = JobType.objects.create(**job_type_data)
# post_a_job.job_type = job_type

# # Create the related instances for job_location
# for location_data in job_location_data:
#     location = JobLocations.objects.create(**location_data)
#     post_a_job.job_location.add(location)

# # # Create the related instances for job_level
# # for level_data in job_level_data:
# #     level = JobLevel.objects.create(**level_data)
# #     post_a_job.job_level.add(level)

# return post_a_job
