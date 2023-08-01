from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from users.serializers.candidate import CandidateRegisterSerializer, CandidatesEmailVerificationSerializer, CandidatesLoginSerializer, CandidateRequestPasswordResetEmailSerializer, CandidatePasswordTokenConfirmSerializer, CandidateSetNewPasswordSerializer, CandidateLogOutSerializer  
from users.utils import Util
from users.models import Candidate

# password reset
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from users.utils import Util

class CandidateRegisterView(GenericAPIView):
    serializer_class = CandidateRegisterSerializer

    def post(self, request):
        user=request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        # Get the email of the current user
        user = Candidate.objects.get(email = user_data['email'])
        # Get access to create a token for the current user
        token = RefreshToken.for_user(user).access_token
        # using the imported modeule, we need to get the current site
        current_site = get_current_site(request).domain
        # using the imported reverse module, we reverse with the url name
        relativeLink = reverse('users:verify_candidate_email')
        # returns the concatenated domain
        absoluteurl = 'http://'+ current_site + relativeLink + "?token=" + str(token)
        email_body = 'Hi, ' + user.username + 'Use link below to verify your email \n' + absoluteurl
        data={'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': user.email,}
        Util.send_email(data)

        return Response(data=user_data, status=status.HTTP_201_CREATED)
    

class VerifyCandidatesEmail(GenericAPIView):
    serializer_class = CandidatesEmailVerificationSerializer

    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user=Candidate.objects.get(id=payload['user_id'])
            if not user.is_email_verified:
                user.is_email_verified = True
                user.save()
            return Response('email: Email verified successfully', status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response('error: Activation link expired', status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response('error: Invalid token', status=status.HTTP_400_BAD_REQUEST)
        
class CandidatesLoginAPIView(GenericAPIView):
    serializer_class = CandidatesLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)   
    
class CandidateRequestPasswordResetEmailView(GenericAPIView):
    serializer_class = CandidateRequestPasswordResetEmailSerializer

    def post(self, request):
        data = {'request': request, 'data': request.data}
        serializer = self.serializer_class(data = data)
        email = request.data['email']
        if Candidate.objects.filter(email = email).exists():
            user = Candidate.objects.get(email = email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relative_link = reverse('users:candidate-password_reset', kwargs={'uidb64': uidb64, 'token': token})
            absolute_url = 'http://'+current_site+relative_link
            email_body= 'Hello, \n Please use the link below to reset your password \n'+ absolute_url
            data={'email_body': email_body, 'email_subject': 'Reset your password', 'to_email': user.email}
            Util.send_email(data)
        return Response({'success': 'A link was sent to your email to reset your password'}, status=status.HTTP_200_OK)


class CandidatePasswordTokenConfirmView(GenericAPIView):
    serializer_class = CandidatePasswordTokenConfirmSerializer
    # def get_serializer_class(self):
    #     return None
    
    # @swagger_auto_schema(auto_schema=False)
    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = Candidate.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'})
            return Response({'sucess': True, 'message': 'Credentials are valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'})

class CandidateSetNewPasswordView(GenericAPIView):
    serializer_class = CandidateSetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        return Response({'success': True, 'message': 'Password reset successfully'}, status=status.HTTP_200_OK)

class CandidateLogOutView(GenericAPIView):
    serializer_class = CandidateLogOutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
