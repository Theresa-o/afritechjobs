from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.serializers.job_skills import JobSkillsSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import JobSkills


@api_view(['GET', 'POST'])
def job_skills(request):
    if request.method == 'GET':
        skills = JobSkills.objects.all()
        skills_list_serializer = JobSkillsSerializer(skills, many=True)
        return Response(skills_list_serializer.data)
    elif request.method == 'POST':
        skills_serializer = JobSkillsSerializer(data=request.data)
        if skills_serializer.is_valid():
            skills_serializer.save()
            return Response(skills_serializer.data, status=status.HTTP_201_CREATED)
        return Response(skills_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_skills_detail(request, id):
    try:
        jobs_skills_detail = JobSkills.objects.get(pk=id)
    except JobSkills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        jobs_skills_detail_serializer = JobSkillsSerializer(jobs_skills_detail)
        return Response(jobs_skills_detail_serializer.data)
    elif request.method == 'PUT':
        jobs_skills_detail_serializer = JobSkillsSerializer(jobs_skills_detail, data=request.data)
        if jobs_skills_detail_serializer.is_valid():
            jobs_skills_detail_serializer.save()
            return Response(jobs_skills_detail_serializer.data)
        return Response(jobs_skills_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        jobs_skills_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)