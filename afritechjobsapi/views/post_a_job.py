from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from afritechjobsapi.filters.filters import PostAJobFilter
from afritechjobsapi.serializers.post_a_job import JobDetailSerializer, JobSerializer
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from afritechjobsapi.models import PostAJob
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination



import logging

logger = logging.getLogger(__name__)

class CustomPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostAJobListView(GenericAPIView):
    # http://127.0.0.1:8000/post-a-job/?search=Machine
    serializer_class = JobSerializer
    queryset = (
        # PostAJob.objects.select_related('job_category', 'job_type', 'created_by')
        PostAJob.objects.select_related('job_category', 'job_type')
        .prefetch_related('job_skills', 'job_location', 'job_level')
        .all()
    )
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    # search_fields = ["job_title", "job_category", "job_skills", "job_type", "job_location", "job_level",]
    search_fields = [
        'job_title',
        'job_category__name', 
        'job_skills__title',
        'job_type__job_type_choices',
        'job_location__name',
        'job_level__job_level_choices'
    ]
    filterset_class = PostAJobFilter
    pagination_class = CustomPagination


    
    def get(self, request, *args, **kwargs):
        # Get the filtered queryset
        queryset = self.filter_queryset(self.get_queryset())

        # Paginate the queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            # If pagination is applied, get the paginated response
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If no pagination, return the full response
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get_queryset(self):
    #     queryset = PostAJob.objects.all()
    #     search_term = self.request.query_params.get('search', None)
    #     if search_term:
    #         queryset = queryset.filter(
    #             Q(job_title__icontains=search_term) |
    #             Q(job_category__name__icontains=search_term) |
    #             Q(job_skills__title__icontains=search_term) |
    #             Q(job_type__job_type_choices__icontains=search_term) |
    #             Q(job_location__name__icontains=search_term) |
    #             Q(job_level__job_level_choices__icontains=search_term)
    #         ).distinct()
    #     return queryset

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned jobs to query parameter in the URL.
    #     """
        
    #     filter_query = Q()
    #     company_name = self.request.query_params.get('company')
    #     if company_name is not None:
    #         filter_query &= Q(company_name__contains=company_name)

    #     user_id = self.request.query_params.get('user_id')
    #     if user_id is not None:
    #         filter_query &= Q(created_by=user_id)

    #     salary = self.request.query_params.get('salary')
    #     if salary is not None:
    #         filter_query &= Q(job_salary_range__gte=salary)

    #     queryset = self.queryset.filter(filter_query)

    #     return queryset
    
    def post(self, request, *args, **kwargs):
        # Instantiate the serializer
        serializer = self.get_serializer(data=request.data)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Create a new instance
        instance = serializer.save()

        # Return serializer
        return_serializer = JobSerializer(instance)

        # Return the serialized data
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)


# class PostAJobView(GenericAPIView):

class PostAJobView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = (
        # PostAJob.objects.select_related('job_category', 'job_type', 'created_by')
        PostAJob.objects.select_related('job_category', 'job_type')
        .prefetch_related('job_skills', 'job_location', 'job_level')
        .all()
    )

    def get(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Instantiate the serializer
        serializer = JobDetailSerializer(instance)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get(self, request, *args, **kwargs):
    #     try:
    #         # Get the model instance
    #         instance = self.get_object()

    #         # Instantiate the serializer
    #         serializer = JobDetailSerializer(instance)

    #         # Return the serialized data
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         logger.error(f"Error in GET request: {e}")
    #         return Response({"detail": "An error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        # Instantiate the serializer
        serializer = self.get_serializer(data=request.data)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Create a new instance
        instance = serializer.save()

        # Return serializer
        return_serializer = JobDetailSerializer(instance)

        # Return the serialized data
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Instantiate the serializer and pass the `partial` arg to it
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        # Perform validation and respond with error messages if failed
        serializer.is_valid(raise_exception=True)

        # Update the instance
        instance = serializer.save()

        # Return serializer
        return_serializer = JobDetailSerializer(instance)

        # Return the serialized data
        return Response(return_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        # Get the model instance
        instance = self.get_object()

        # Simply delete - no need to instantiate the serializer
        instance.delete()

        # Return an empty response
        return Response({}, status=status.HTTP_204_NO_CONTENT)