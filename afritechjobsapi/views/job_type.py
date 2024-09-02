from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.filters.filters import JobTypeFilter
from afritechjobsapi.serializers.job_type import JobTypeSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import JobType



@api_view(['GET'])
def job_type(request):
    if request.method == 'GET':
        type = JobType.objects.all()
        filterset = JobTypeFilter(request.GET, queryset=type)
        if filterset.is_valid():
            type = filterset.qs
        type_list_serializer = JobTypeSerializer(type, many=True)
        return Response(type_list_serializer.data)