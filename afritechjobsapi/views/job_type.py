from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.filters.filters import JobTypeFilter
from afritechjobsapi.serializers.job_type import JobTypeSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import JobType
from rest_framework.pagination import PageNumberPagination




@api_view(['GET'])
def job_type(request):
    if request.method == 'GET':
        type = JobType.objects.all()
        filterset = JobTypeFilter(request.GET, queryset=type)
        if filterset.is_valid():
            type = filterset.qs

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        paginator.page_size_query_param = 'page_size' 
        paginator.max_page_size = 100
        paginated_type= paginator.paginate_queryset(type, request)

        type_list_serializer = JobTypeSerializer(paginated_type, many=True)
        # Return paginated response
        return paginator.get_paginated_response(type_list_serializer.data)