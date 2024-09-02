from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.filters.filters import JobLevelFilter
from afritechjobsapi.serializers.job_level import JobLevelSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import JobLevel

@api_view(['GET'])
def job_level(request):
    if request.method == 'GET':
        level = JobLevel.objects.all()
        filterset = JobLevelFilter(request.GET, queryset=level)
        if filterset.is_valid():
            level = filterset.qs
        level_list_serializer = JobLevelSerializer(level, many=True)
        return Response(level_list_serializer.data)