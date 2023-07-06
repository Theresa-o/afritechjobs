from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from afritechjobsapi.serializers.post_a_job import JobDetailSerializer, JobSerializer
from afritechjobsapi.serializers.blog import BlogSerializer
from afritechjobsapi.serializers.event import EventSerializer
from afritechjobsapi.serializers.workresources import WorkResourcesSerializer
from afritechjobsapi.serializers.hiringguide import HiringGuideSerializer
from afritechjobsapi.serializers.category import CategorySerializer
from afritechjobsapi.serializers.job_skills import JobSkillsSerializer
from afritechjobsapi.serializers.job_location import JobLocationsSerializer
from afritechjobsapi.serializers.job_type import JobTypeSerializer
from afritechjobsapi.serializers.job_level import JobLevelSerializer
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import (
    Profile,
    Blog,
    Event,
    WorkResources,
    HiringGuide,
    PostAJob,
    Category,
    JobSkills,
    JobLocations,
    JobType,
    JobLevel,
)

# from afritechjobsapi.serializers import (
#     # BlogSerializer,
#     # EventSerializer,
#     # WorkResourcesSerializer,
#     # HiringGuideSerializer,
#     # PostAJobSerializer,
#     # JobSerializer,
#     # CategorySerializer,
#     # JobSkillsSerializer,
#     # JobLocationsSerializer,
#     # JobTypeSerializer,
#     # JobLevelSerializer,

#     # JobDetailSerializer, 
#     # JobSerializer
# )


@api_view(['GET', 'POST'])
def blog_list(request, format=None):
    if request.method == 'GET':
        blog = Blog.objects.all()
        blog_list_serializer = BlogSerializer(blog, many=True)
        return Response(blog_list_serializer.data)
    elif request.method == 'POST':
        blog_list_serializer = BlogSerializer(data=request.data)
        if blog_list_serializer.is_valid():
            blog_list_serializer.save()
            return Response(blog_list_serializer.data, status=status.HTTP_201_CREATED)
        return Response(blog_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, id, format=None):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        blog_detail_serializer = BlogSerializer(blog)
        return Response(blog_detail_serializer.data)
    elif request.method == 'PUT':
        blog_detail_serializer = BlogSerializer(blog, data=request.data)
        if blog_detail_serializer.is_valid():
            blog_detail_serializer.save()
            return Response(blog_detail_serializer.data)
        return Response(blog_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def event_list(request):
    if request.method == 'GET':
        event = Event.objects.all()
        event_list_serializer = EventSerializer(event, many=True)
        return Response(event_list_serializer.data)
    elif request.method == 'POST':
        event_list_serializer = EventSerializer(data=request.data)
        if event_list_serializer.is_valid():
            event_list_serializer.save()
            return Response(event_list_serializer.data, status=status.HTTP_201_CREATED)
        return Response(event_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, id, format=None):
    try:
        event = Event.objects.get(pk=id)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        event_detail_serializer = EventSerializer(event)
        return Response(event_detail_serializer.data)
    elif request.method == 'PUT':
        event_detail_serializer = EventSerializer(event, data=request.data)
        if event_detail_serializer.is_valid():
            event_detail_serializer.save()
            return Response(event_detail_serializer.data)
        return Response(event_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def work_resources_list(request, format=None):
    if request.method == 'GET':
        work_resources = WorkResources.objects.all()
        work_resources_list_serializer = WorkResourcesSerializer(work_resources, many=True)
        return Response(work_resources_list_serializer.data)
    elif request.method == 'POST':
        work_resources_list_serializer = WorkResourcesSerializer(data=request.data)
        if work_resources_list_serializer.is_valid():
            work_resources_list_serializer.save()
            return Response(work_resources_list_serializer.data, status=status.HTTP_201_CREATED)
        return Response(work_resources_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def work_resources_detail(request, id):
    try:
        work_resources = WorkResources.objects.get(pk=id)
    except WorkResources.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        work_resources_details_serializer = WorkResourcesSerializer(work_resources)
        return Response(work_resources_details_serializer.data)
    elif request.method == 'PUT':
        work_resources_details_serializer = WorkResourcesSerializer(work_resources, data=request.data)
        if work_resources_details_serializer.is_valid():
            work_resources_details_serializer.save()
            return Response(work_resources_details_serializer.data)
        return Response(work_resources_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        work_resources.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def hiring_guide_list(request, format=None):
    if request.method == 'GET':
        hiring_guide = HiringGuide.objects.all()
        hiring_guide_list_serializer = HiringGuideSerializer(hiring_guide, many=True)
        return Response(hiring_guide_list_serializer.data)
    elif request.method == 'POST':
        hiring_guide_list_serializer = HiringGuideSerializer(data=request.data)
        if hiring_guide_list_serializer.is_valid():
            hiring_guide_list_serializer.save()
            return Response(hiring_guide_list_serializer.data, status=status.HTTP_201_CREATED)
        return Response(hiring_guide_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def hiring_guide_detail(request, id):
    try:
        hiring_guide = HiringGuide.objects.get(pk=id)
    except HiringGuide.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        hiring_guide_details_serializer = HiringGuideSerializer(hiring_guide)
        return Response(hiring_guide_details_serializer.data)
    elif request.method == 'PUT':
        hiring_guide_details_serializer = HiringGuideSerializer(hiring_guide, data=request.data)
        if hiring_guide_details_serializer.is_valid():
            hiring_guide_details_serializer.save()
            return Response(hiring_guide_details_serializer.data)
        return Response(hiring_guide_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        hiring_guide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def job_category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        category_list_serializer = CategorySerializer(category, many=True)
        return Response(category_list_serializer.data)
    elif request.method == 'POST':
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_201_CREATED)
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_category_detail(request, id):
    try:
        jobs_category_detail = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        jobs_category_detail_serializer = CategorySerializer(jobs_category_detail)
        return Response(jobs_category_detail_serializer.data)
    elif request.method == 'PUT':
        jobs_category_detail_serializer = CategorySerializer(jobs_category_detail, data=request.data)
        if jobs_category_detail_serializer.is_valid():
            jobs_category_detail_serializer.save()
            return Response(jobs_category_detail_serializer.data)
        return Response(jobs_category_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        jobs_category_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def job_skills(request):
    if request.method == 'GET':
        skills = JobSkills.objects.all()
        skills_list_serializer = JobSkillsSerializer(skills, many=True)
        return Response(skills_list_serializer.data)
    elif request.method == 'POST':
        skills_serializer = JobSkillsSerializer(data=request.data)
        if skills_serializer.is_valid():
            skills_serializer.save()
            return Response(skills_serializer.data, status=status.HTTP_201_CREATED)
        return Response(skills_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_skills_detail(request, id):
    try:
        jobs_skills_detail = JobSkills.objects.get(pk=id)
    except JobSkills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        jobs_skills_detail_serializer = JobSkillsSerializer(jobs_skills_detail)
        return Response(jobs_skills_detail_serializer.data)
    elif request.method == 'PUT':
        jobs_skills_detail_serializer = JobSkillsSerializer(jobs_skills_detail, data=request.data)
        if jobs_skills_detail_serializer.is_valid():
            jobs_skills_detail_serializer.save()
            return Response(jobs_skills_detail_serializer.data)
        return Response(jobs_skills_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        jobs_skills_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def job_locations(request):
    if request.method == 'GET':
        locations = JobLocations.objects.all()
        locations_list_serializer = JobLocationsSerializer(locations, many=True)
        return Response(locations_list_serializer.data)
    elif request.method == 'POST':
        locations_serializer = JobLocationsSerializer(data=request.data)
        if locations_serializer.is_valid():
            locations_serializer.save()
            return Response(locations_serializer.data, status=status.HTTP_201_CREATED)
        return Response(locations_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_locations_detail(request, id):
    try:
        jobs_locations_detail = JobLocations.objects.get(pk=id)
    except JobLocations.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        jobs_locations_detail_serializer = JobLocationsSerializer(jobs_locations_detail)
        return Response(jobs_locations_detail_serializer.data)
    elif request.method == 'PUT':
        jobs_locations_detail_serializer = JobLocationsSerializer(jobs_locations_detail, data=request.data)
        if jobs_locations_detail_serializer.is_valid():
            jobs_locations_detail_serializer.save()
            return Response(jobs_locations_detail_serializer.data)
        return Response(jobs_locations_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        jobs_locations_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def job_type(request):
    if request.method == 'GET':
        type = JobType.objects.all()
        type_list_serializer = JobTypeSerializer(type, many=True)
        return Response(type_list_serializer.data)


@api_view(['GET'])
def job_level(request):
    if request.method == 'GET':
        level = JobLevel.objects.all()
        level_list_serializer = JobLevelSerializer(level, many=True)
        return Response(level_list_serializer.data)


# @api_view(['POST'])
# def post_a_job(request):
#     if request.method == 'POST':
#         post_a_job_serializer = PostAJobSerializer(data=request.data)
#         # print(request.data)
#         post_a_job_serializer.is_valid(raise_exception=True)
#         validated_data = post_a_job_serializer.validated_data
#         job = PostAJob.objects.create(
#             job_title=validated_data['job_title'],
#             job_salary_range=validated_data['job_salary_range'],
#             job_description=validated_data['job_description'],
#             job_application_link=validated_data['job_application_link'],
#             company_name=validated_data['company_name'],
#             company_hq=validated_data['company_hq'],
#             companys_website=validated_data['companys_website'],
#             company_contact_email=validated_data['company_contact_email'],
#             company_description=validated_data['company_description'],
#             job_category=Category.objects.get(id=validated_data['job_category_id']),
#             job_type=JobType.objects.get(id=validated_data['job_type_id']),
#             created_by=get_user_model().objects.get(id=validated_data['created_by_id']),
#         )
#         for skill in JobSkills.objects.filter(id__in=validated_data['job_skills_id']):
#             job.job_skills.add(skill)
#         for location in JobLocations.objects.filter(id__in=validated_data['job_location_id']):
#             job.job_location.add(location)
#         for level in JobLevel.objects.filter(id__in=validated_data['job_level_id']):
#             job.job_level.add(level)

#         # saving instance
#         job.save()
#         job_serializer = JobSerializer(job)
#         return Response(job_serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def view_jobs(request):
#     if request.method == 'GET':
#         post_a_job = PostAJob.objects.all()
#         post_a_job_serializer = PostAJobSerializer(post_a_job, many=True)
#         return Response(post_a_job_serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def view_jobs_detail(request, id):
#     try:
#         view_jobs_detail = PostAJob.objects.get(pk=id)
#     except PostAJob.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         view_jobs_detail_serializer = PostAJobSerializer(view_jobs_detail)
#         return Response(view_jobs_detail_serializer.data)
#     elif request.method == 'PUT':
#         view_jobs_detail_serializer = PostAJobSerializer(view_jobs_detail, data=request.data)
#         if view_jobs_detail_serializer.is_valid():
#             view_jobs_detail_serializer.save()
#             return Response(view_jobs_detail_serializer.data)
#         return Response(view_jobs_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         view_jobs_detail.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class PostAJobListView(GenericAPIView):
    serializer_class = JobDetailSerializer
    queryset = (
        PostAJob.objects.select_related('job_category', 'job_type', 'created_by')
        .prefetch_related('job_skills', 'job_location', 'job_level')
        .all()
    )

    def get(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.get_queryset()

        # Instantiate the serializer
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """
        Optionally restricts the returned jobs to query parameter in the URL.
        """
        
        filter_query = Q()
        company_name = self.request.query_params.get('company')
        if company_name is not None:
            filter_query &= Q(company_name__contains=company_name)

        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            filter_query &= Q(created_by=user_id)

        salary = self.request.query_params.get('salary')
        if salary is not None:
            filter_query &= Q(job_salary_range__gte=salary)

        queryset = self.queryset.filter(filter_query)

        return queryset


class PostAJobView(GenericAPIView):
    serializer_class = JobSerializer
    queryset = (
        PostAJob.objects.select_related('job_category', 'job_type', 'created_by')
        .prefetch_related('job_skills', 'job_location', 'job_level')
        .all()
    )

    def get(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Instantiate the serializer
        serializer = JobDetailSerializer(instance)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # Instantiate the serializer
        serializer = self.get_serializer(data=request.data)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Create a new instance
        instance = serializer.save()

        # Return serializer
        return_serializer = JobDetailSerializer(instance)

        # Return the serialized data
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Instantiate the serializer and pass the `partial` arg to it
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Update the instance
        instance = serializer.save()

        # Return serializer
        return_serializer = JobDetailSerializer(instance)

        # Return the serialized data
        return Response(return_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Simply delete - no need to instantiate the serializer
        instance.delete()

        # Return an empty response
        return Response({}, status=status.HTTP_204_NO_CONTENT)
