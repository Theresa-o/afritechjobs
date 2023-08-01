from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.serializers.workresources import WorkResourcesSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import WorkResources


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