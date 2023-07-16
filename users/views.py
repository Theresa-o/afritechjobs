from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from users.serializers import RegisterSerializer, RecruiterRegisterSerializer, CandidateRegisterSerializer
# from users.models import EmailConfirmationToken, User
# from users.utils import send_confirmation_email, Util
from users.utils import Util
from users.models import User


#TODO: Account gets created even if the persons has not verified yet, as soon as POST is created, it creates
#TODO: Put the EMAIL_HOST_USER and password in an env file, not directly into settings
# Create your views here.

class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])
        # get token to be used by user
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse('users:verify-email')
        absolute_url = 'http://'+current_site+relative_link+"?token="+str(token)
        email_body= 'Hello ' + user.username +'\nPlease verify your email using the link below \n'+ absolute_url
        data={'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': user.email}
        Util.send_email(data)
        return Response(data=user_data, status=status.HTTP_201_CREATED)


    
class VerifyEmail(GenericAPIView):
    def get(self):
        pass
    
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
    


