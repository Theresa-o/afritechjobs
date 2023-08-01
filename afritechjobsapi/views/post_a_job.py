from rest_framework.response import Response
from afritechjobsapi.serializers.post_a_job import JobDetailSerializer, JobSerializer
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from afritechjobsapi.models import PostAJob




class PostAJobListView(GenericAPIView):
    serializer_class = JobDetailSerializer
    queryset = (
        PostAJob.objects.select_related('job_category', 'job_type', 'created_by')
        .prefetch_related('job_skills', 'job_location', 'job_level')
        .all()
    )

    def get(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.get_queryset()

        # Instantiate the serializer
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """
        Optionally restricts the returned jobs to query parameter in the URL.
        """
        
        filter_query = Q()
        company_name = self.request.query_params.get('company')
        if company_name is not None:
            filter_query &= Q(company_name__contains=company_name)

        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            filter_query &= Q(created_by=user_id)

        salary = self.request.query_params.get('salary')
        if salary is not None:
            filter_query &= Q(job_salary_range__gte=salary)

        queryset = self.queryset.filter(filter_query)

        return queryset
    
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


class PostAJobView(GenericAPIView):
    serializer_class = JobSerializer
    queryset = (
        PostAJob.objects.select_related('job_category', 'job_type', 'created_by')
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