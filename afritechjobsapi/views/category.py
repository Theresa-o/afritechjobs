from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.serializers.category import CategorySerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import Category


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