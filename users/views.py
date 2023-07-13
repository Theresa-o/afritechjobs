from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer, RecruiterRegisterSerializer, CandidateRegisterSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(data=user_data, status=status.HTTP_201_CREATED)
    
class RecruiterRegisterView(GenericAPIView):

    serializer_class = RecruiterRegisterSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(data=user_data, status=status.HTTP_201_CREATED)
    
class CandidateRegisterView(GenericAPIView):

    serializer_class = CandidateRegisterSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(data=user_data, status=status.HTTP_201_CREATED)

