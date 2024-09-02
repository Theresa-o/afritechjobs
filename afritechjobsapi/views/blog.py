from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.serializers.blog import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import Blog


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
    

