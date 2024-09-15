from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.filters.filters import JobLocationsFilter
from afritechjobsapi.serializers.job_location import JobLocationsSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import JobLocations
from rest_framework.pagination import PageNumberPagination


@api_view(['GET', 'POST'])
def job_locations(request):
    if request.method == 'GET':
        locations = JobLocations.objects.all()
        filterset = JobLocationsFilter(request.GET, queryset=locations)
        if filterset.is_valid():
            locations = filterset.qs

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        paginator.page_size_query_param = 'page_size' 
        paginator.max_page_size = 100
        paginated_locations= paginator.paginate_queryset(locations, request)

        locations_list_serializer = JobLocationsSerializer(paginated_locations, many=True)

        # Return paginated response
        return paginator.get_paginated_response(locations_list_serializer.data)
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