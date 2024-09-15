from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.filters.filters import JobLevelFilter
from afritechjobsapi.serializers.job_level import JobLevelSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import JobLevel
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def job_level(request):
    if request.method == 'GET':
        level = JobLevel.objects.all()
        filterset = JobLevelFilter(request.GET, queryset=level)
        if filterset.is_valid():
            level = filterset.qs

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        paginator.page_size_query_param = 'page_size' 
        paginator.max_page_size = 100
        paginated_level = paginator.paginate_queryset(level, request)

        level_list_serializer = JobLevelSerializer(paginated_level, many=True)
        
        # Return paginated response
        return paginator.get_paginated_response(level_list_serializer.data)