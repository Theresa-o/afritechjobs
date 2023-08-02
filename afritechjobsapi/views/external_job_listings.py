from afritechjobsapi.models import ExternalJobListing
from afritechjobsapi.serializers import ExternalJobListingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json

#TODO: Using caching or a different method to make sure that when data exist in database, a user does not have to start the process of retrieving data from the start
#TODO: Use celery to make cron job request 


class ExternalJobListView(APIView):
    """
    List all jobs gotten from external api.
    This view make and external api call, save the result and return the data generated as json object 
    """
    def get(self, request, format=None):
        url = 'https://www.getonbrd.com/api/v0/jobs?per_page=10&page=1&api_key=a1b2c3d4e5f6g7h8klmnpo'
        response = requests.get(url)
        response_status = response.status_code
        if response_status == 200:
            data = response.json
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    

# class ExternalJobDetailView(APIView):
#     """
#     Retrieve an external job instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)