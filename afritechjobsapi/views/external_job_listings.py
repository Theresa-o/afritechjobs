from afritechjobsapi.models import ExternalJobListing
# from afritechjobsapi.serializers import ExternalJobListingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import requests
import json

#TODO: Using caching or a different method to make sure that when data exist in database, a user does not have to start the process of retrieving data from the start
#TODO: Use celery to make cron job request 
#TODO: Group each external data into category and if it falls into any of our internal category, let it be displayed in that category list

class SecondExternalJobListView(APIView):
    """
    List all jobs gotten from external api.
    This view makes an external API call, saves the result, and returns the data as a JSON object.
    """
    def get(self, request, format=None):
        url = "https://remotive.com/api/remote-jobs"
        response = requests.get(url)
        response_status = response.status_code
        if response_status == 200:
            data = response.json()
            filtered_jobs = []
            # Filter jobs with "candidate_required_location" == "Worldwide"
            # filtered_jobs = [job for job in data["jobs"] if job["candidate_required_location"] == "Worldwide"]
            # return Response(filtered_jobs, status=status.HTTP_200_OK)
        
            for job in data['jobs']:
                if job["candidate_required_location"] == "Worldwide":
                    # if job["category"] == "Software Development":
                    # if job["job_type"] == "full_time":
                    filtered_jobs.append(job)
                return Response(filtered_jobs, status=status.HTTP_200_OK)
        else:
            return Response('error', status=status.HTTP_404_NOT_FOUND)

# class ExternalJobListView(APIView):
#     """
#     List all jobs gotten from external api.
#     This view make and external api call, save the result and return the data generated as json object 
#     """
#     def get(self, request, format=None):
#         # url = 'https://www.getonbrd.com/api/v0/jobs?per_page=10&page=1&api_key=a1b2c3d4e5f6g7h8klmnpo'
#         url = "https://www.getonbrd.com/api/v0/jobs?per_page=10&page=1&api_key=a1b2c3d4e5f6g7h8klmnpo"
#         payload={}
#         headers = {}
#         # response = requests.get(url, headers=headers, data=payload)
#         response = requests.request("GET", url, headers=headers, data=payload)
#         print(response.text)
#         response_status = response.status_code
#         if response_status == 200:
#             data = response.json
#             print(data.text)
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

class ExternalJobListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        url = "https://www.getonbrd.com/api/v0/jobs"
        headers = {
            "Authorization": "Bearer a1b2c3d4e5f6g7h8klmnpo"
        }
        params = {
            "per_page": 10,
            "page": 1
        }
        response = requests.get(url, headers=headers, params=params)
        print(response.text)

        if response.status_code == 200:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response('error', status=status.HTTP_404_NOT_FOUND)
    

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