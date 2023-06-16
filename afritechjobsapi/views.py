from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Blog, Event, WorkResources, HiringGuide, PostAJob, Category, JobSkills, JobLocations, JobType, JobLevel
from .serializers import BlogSerializer, EventSerializer, WorkResourcesSerializer, HiringGuideSerializer, PostAJobSerializer, CategorySerializer, JobSkillsSerializer, JobLocationsSerializer, JobTypeSerializer, JobLevelSerializer

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

@api_view(['POST'])
def post_a_job(request):
    if request.method == 'POST':
        post_a_job_serializer = PostAJobSerializer(data=request.data)
        print(request.data)
        if post_a_job_serializer.is_valid():
            print(request.data)
            post_a_job_serializer.save()
            return Response(post_a_job_serializer.data, status=status.HTTP_201_CREATED)
        return Response(post_a_job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def view_jobs(request):
    if request.method == 'GET':
        post_a_job = PostAJob.objects.all()
        post_a_job_serializer = PostAJobSerializer(post_a_job, many=True)
        return Response(post_a_job_serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def view_jobs_detail(request, id):
    try:
        view_jobs_detail = PostAJob.objects.get(pk=id)
    except PostAJob.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        view_jobs_detail_serializer = PostAJobSerializer(view_jobs_detail)
        return Response(view_jobs_detail_serializer.data)
    elif request.method == 'PUT':
        view_jobs_detail_serializer = PostAJobSerializer(view_jobs_detail, data=request.data)
        if view_jobs_detail_serializer.is_valid():
            view_jobs_detail_serializer.save()
            return Response(view_jobs_detail_serializer.data)
        return Response(view_jobs_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        view_jobs_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)