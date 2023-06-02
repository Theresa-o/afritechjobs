from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Blog, Event, WorkResources
from .serializers import BlogSerializer, EventSerializer

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




