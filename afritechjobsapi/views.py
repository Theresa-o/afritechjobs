from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import CreateJobForm
from .models import Profile, Blog, Event, WorkResources, HiringGuide, PostAJob
from .serializers import BlogSerializer, EventSerializer, WorkResourcesSerializer, HiringGuideSerializer, PostAJobSerializer

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

@api_view(['POST'])
def post_a_job(request):
    # if request.method == 'GET':
    #     post_a_job = PostAJob.objects.all()
    #     post_a_job_serializer = PostAJobSerializer(post_a_job, many=True)
    #     return Response(post_a_job_serializer.data)

    #method 1
    # if request.method == 'POST':
    #     post_a_job_serializer = PostAJobSerializer(data=request.data)
    #     if post_a_job_serializer.is_valid():
    #         post_a_job_serializer.save()
    #         return Response(post_a_job_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(post_a_job_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #method2
    if request.method == 'POST':
        form = CreateJobForm(request.data)
        if form.is_valid():
            create_job = form.save(commit=False)
            create_job.created_by = request.user
            create_job.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
