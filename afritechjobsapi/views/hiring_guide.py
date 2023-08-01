from rest_framework.decorators import api_view
from rest_framework.response import Response
from afritechjobsapi.serializers.hiringguide import HiringGuideSerializer
from rest_framework import status
from rest_framework.response import Response
from afritechjobsapi.models import HiringGuide

@api_view(['GET', 'POST'])
def hiring_guide_list(request, format=None):
    if request.method == 'GET':
        hiring_guide = HiringGuide.objects.all()
        hiring_guide_list_serializer = HiringGuideSerializer(hiring_guide, many=True)
        return Response(hiring_guide_list_serializer.data)
    elif request.method == 'POST':
        hiring_guide_list_serializer = HiringGuideSerializer(data=request.data)
        if hiring_guide_list_serializer.is_valid():
            hiring_guide_list_serializer.save()
            return Response(hiring_guide_list_serializer.data, status=status.HTTP_201_CREATED)
        return Response(hiring_guide_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def hiring_guide_detail(request, id):
    try:
        hiring_guide = HiringGuide.objects.get(pk=id)
    except HiringGuide.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        hiring_guide_details_serializer = HiringGuideSerializer(hiring_guide)
        return Response(hiring_guide_details_serializer.data)
    elif request.method == 'PUT':
        hiring_guide_details_serializer = HiringGuideSerializer(hiring_guide, data=request.data)
        if hiring_guide_details_serializer.is_valid():
            hiring_guide_details_serializer.save()
            return Response(hiring_guide_details_serializer.data)
        return Response(hiring_guide_details_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        hiring_guide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)