# from django.shortcuts import render
# from rest_framework.generics import GenericAPIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# import jwt
# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse
# from django.conf import settings
# from drf_yasg.utils import swagger_auto_schema
# from drf_yasg import openapi

# from users.serializers.administrator import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, RequestPasswordResetEmailSerializer, SetNewPasswordSerializer, LogOutSerializer, PasswordTokenConfirmSerializer
# from users.serializers.recruiter import RecruiterRegisterSerializer, RecruiterEmailVerificationSerializer, RecruiterLoginSerializer, RecruiterRequestPasswordResetEmailSerializer, RecruiterPasswordTokenConfirmSerializer, RecruiterSetNewPasswordSerializer, RecruiterLogOutSerializer
# from users.serializers.candidate import CandidateRegisterSerializer, CandidatesEmailVerificationSerializer, CandidatesLoginSerializer, CandidateRequestPasswordResetEmailSerializer, CandidatePasswordTokenConfirmSerializer, CandidateSetNewPasswordSerializer, CandidateLogOutSerializer  
# from users.utils import Util
# from users.models import User, Recruiter, Candidate

# # password reset
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.contrib.sites.shortcuts import get_current_site
# from django.urls import reverse
# from users.utils import Util, RecruiterUtil


# #TODO: Account gets created even if the persons has not verified yet, as soon as POST is created, it creates
# #TODO: Put the EMAIL_HOST_USER and password in an env file, not directly into settings
# #TODO: Older things like blogs, hiring guides not showing parameters for swagger
# #TODO: Create a cron job that removes the blocklisted tokens for logout by calling flushexpiredtokens - check jwt doc and cryce video
# #TODO: the login details for admin user can be used on recruiter login and vice versa #make sure this does not work
# #TODO: Password used before can be reused immediately after for password reset, make sure that the user puts in a new password different from the previous one
# #TODO: Using John explanation on stackoverflow, add celery to email sending job - https://stackoverflow.com/questions/76772897/timeouterror-winerror-10060-a-connection-attempt-failed-because-the-connected#76773941 and https://stackoverflow.com/questions/64678689/i-am-sending-registration-activation-email-using-celery-in-django-but-celery-giv
#TODO: Create tags to make search search easier and to be included in the job posting for easy scannability
#TODO: Add test to the functions



# class RegisterView(GenericAPIView):

#     serializer_class = RegisterSerializer

#     def post(self, request):
#         user=request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         user_data = serializer.data

#         user = User.objects.get(email=user_data['email'])
#         # get token to be used by user
#         token = RefreshToken.for_user(user).access_token

#         current_site = get_current_site(request).domain
#         relative_link = reverse('users:verify-email')
#         absolute_url = 'http://'+current_site+relative_link+"?token="+str(token)
#         email_body= 'Hello ' + user.username +'\nPlease verify your email using the link below \n'+ absolute_url
#         data={'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': user.email}
#         Util.send_email(data)
#         return Response(data=user_data, status=status.HTTP_201_CREATED)


    
# class VerifyEmail(APIView):
#     serializer_class = EmailVerificationSerializer

#     token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
#     @swagger_auto_schema(manual_parameters=[token_param_config])
#     def get(self, request):
#         token = request.GET.get('token')
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user=User.objects.get(id=payload['user_id'])
#             if not user.is_email_verified:
#                 user.is_email_verified = True
#                 user.save()
#             return Response('email: Email verified successfully', status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError as identifier:
#             return Response('error: Activation link expired', status=status.HTTP_400_BAD_REQUEST)
#         except jwt.exceptions.DecodeError as identifier:
#             return Response('error: Invalid token', status=status.HTTP_400_BAD_REQUEST)
        
# class LoginAPIView(GenericAPIView):
#     serializer_class = LoginSerializer
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

# class RequestPasswordResetEmailView(GenericAPIView):
#     serializer_class = RequestPasswordResetEmailSerializer

#     def post(self, request):
#         data = {'request': request, 'data': request.data}
#         serializer = self.serializer_class(data = data)
#         email = request.data['email']
#         if User.objects.filter(email = email).exists():
#             user = User.objects.get(email = email)
#             uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
#             token = PasswordResetTokenGenerator().make_token(user)
#             current_site = get_current_site(request=request).domain
#             relative_link = reverse('users:password_reset', kwargs={'uidb64': uidb64, 'token': token})
#             absolute_url = 'http://'+current_site+relative_link
#             email_body= 'Hello, \n Please use the link below to reset your password \n'+ absolute_url
#             data={'email_body': email_body, 'email_subject': 'Reset your password', 'to_email': user.email}
#             Util.send_email(data)
#         return Response({'success': 'A link was sent to your email to reset your password'}, status=status.HTTP_200_OK)


# class PasswordTokenConfirmView(GenericAPIView):
#     serializer_class = PasswordTokenConfirmSerializer
#     # def get_serializer_class(self):
#     #     return None
    
#     # @swagger_auto_schema(auto_schema=False)
#     def get(self, request, uidb64, token):
        
#         try:
#             id = smart_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(id=id)

#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'})
#             return Response({'sucess': True, 'message': 'Credentials are valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

#         except DjangoUnicodeDecodeError as identifier:
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'})
        
#     # def get_queryset(self):
#     #     if getattr(self, 'swagger_fake_view', False):
#     #         # queryset just for schema generation metadata
#     #         return User.objects.none()
        
#     # def get_serializer_class(self):
#     #     return None
        
# class SetNewPasswordView(GenericAPIView):
#     serializer_class = SetNewPasswordSerializer

#     def patch(self, request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         return Response({'success': True, 'message': 'Password reset successfully'}, status=status.HTTP_200_OK)
    
# class LogOutView(GenericAPIView):
#     serializer_class = LogOutSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)






# # -----------------------------RECRUITERS-----------------------------
    
# class RecruiterRegisterView(GenericAPIView):

#     serializer_class = RecruiterRegisterSerializer

#     def post(self, request):
#         user=request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         # Get the email of the current user
#         user = Recruiter.objects.get(email = user_data['email'])
#         # Get access to create a token for the current user
#         token = RefreshToken.for_user(user).access_token
#         # using the imported modeule, we need to get the current site
#         current_site = get_current_site(request).domain
#         # using the imported reverse module, we reverse with the url name
#         relativeLink = reverse('users:verify_recruiter_email')
#         # returns the concatenated domain
#         absoluteurl = 'http://'+ current_site + relativeLink + "?token=" + str(token)
#         email_body = 'Hi, ' + user.username + 'Use link below to verify your email \n' + absoluteurl
#         data={'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': user.email,}
#         RecruiterUtil.send_email(data)

#         return Response(data=user_data, status=status.HTTP_201_CREATED)
    
# class VerifyRecruiterEmail(GenericAPIView):
#     serializer_class = RecruiterEmailVerificationSerializer

#     token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
#     @swagger_auto_schema(manual_parameters=[token_param_config])
#     def get(self, request):
#         token = request.GET.get('token')
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user=Recruiter.objects.get(id=payload['user_id'])
#             if not user.is_email_verified:
#                 user.is_email_verified = True
#                 user.save()
#             return Response('email: Email verified successfully', status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError as identifier:
#             return Response('error: Activation link expired', status=status.HTTP_400_BAD_REQUEST)
#         except jwt.exceptions.DecodeError as identifier:
#             return Response('error: Invalid token', status=status.HTTP_400_BAD_REQUEST)

# class RecruiterLoginAPIView(GenericAPIView):
#     serializer_class = RecruiterLoginSerializer
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)    
    
# class RecruiterRequestPasswordResetEmailView(GenericAPIView):
#     serializer_class = RecruiterRequestPasswordResetEmailSerializer

#     def post(self, request):
#         data = {'request': request, 'data': request.data}
#         serializer = self.serializer_class(data = data)
#         email = request.data['email']
#         if Recruiter.objects.filter(email = email).exists():
#             user = Recruiter.objects.get(email = email)
#             uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
#             token = PasswordResetTokenGenerator().make_token(user)
#             current_site = get_current_site(request=request).domain
#             relative_link = reverse('users:recruiter-password_reset', kwargs={'uidb64': uidb64, 'token': token})
#             absolute_url = 'http://'+current_site+relative_link
#             email_body= 'Hello, \n Please use the link below to reset your password \n'+ absolute_url
#             data={'email_body': email_body, 'email_subject': 'Reset your password', 'to_email': user.email}
#             RecruiterUtil.send_email(data)
#         return Response({'success': 'A link was sent to your email to reset your password'}, status=status.HTTP_200_OK)


# class RecruiterPasswordTokenConfirmView(GenericAPIView):
#     serializer_class = RecruiterPasswordTokenConfirmSerializer
#     # def get_serializer_class(self):
#     #     return None
    
#     # @swagger_auto_schema(auto_schema=False)
#     def get(self, request, uidb64, token):
        
#         try:
#             id = smart_str(urlsafe_base64_decode(uidb64))
#             user = Recruiter.objects.get(id=id)

#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'})
#             return Response({'sucess': True, 'message': 'Credentials are valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

#         except DjangoUnicodeDecodeError as identifier:
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'})

# class RecruiterSetNewPasswordView(GenericAPIView):
#     serializer_class = RecruiterSetNewPasswordSerializer

#     def patch(self, request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         return Response({'success': True, 'message': 'Password reset successfully'}, status=status.HTTP_200_OK)

# class RecruiterLogOutView(GenericAPIView):
#     serializer_class = RecruiterLogOutSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# # -----------------------------------CANDIDATES--------------------
    
# class CandidateRegisterView(GenericAPIView):
#     serializer_class = CandidateRegisterSerializer

#     def post(self, request):
#         user=request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#         # Get the email of the current user
#         user = Candidate.objects.get(email = user_data['email'])
#         # Get access to create a token for the current user
#         token = RefreshToken.for_user(user).access_token
#         # using the imported modeule, we need to get the current site
#         current_site = get_current_site(request).domain
#         # using the imported reverse module, we reverse with the url name
#         relativeLink = reverse('users:verify_candidate_email')
#         # returns the concatenated domain
#         absoluteurl = 'http://'+ current_site + relativeLink + "?token=" + str(token)
#         email_body = 'Hi, ' + user.username + 'Use link below to verify your email \n' + absoluteurl
#         data={'email_body': email_body, 'email_subject': 'Verify your email', 'to_email': user.email,}
#         Util.send_email(data)

#         return Response(data=user_data, status=status.HTTP_201_CREATED)
    

# class VerifyCandidatesEmail(GenericAPIView):
#     serializer_class = CandidatesEmailVerificationSerializer

#     token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)
#     @swagger_auto_schema(manual_parameters=[token_param_config])
#     def get(self, request):
#         token = request.GET.get('token')
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#             user=Candidate.objects.get(id=payload['user_id'])
#             if not user.is_email_verified:
#                 user.is_email_verified = True
#                 user.save()
#             return Response('email: Email verified successfully', status=status.HTTP_200_OK)
#         except jwt.ExpiredSignatureError as identifier:
#             return Response('error: Activation link expired', status=status.HTTP_400_BAD_REQUEST)
#         except jwt.exceptions.DecodeError as identifier:
#             return Response('error: Invalid token', status=status.HTTP_400_BAD_REQUEST)
        
# class CandidatesLoginAPIView(GenericAPIView):
#     serializer_class = CandidatesLoginSerializer
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)   
    
# class CandidateRequestPasswordResetEmailView(GenericAPIView):
#     serializer_class = CandidateRequestPasswordResetEmailSerializer

#     def post(self, request):
#         data = {'request': request, 'data': request.data}
#         serializer = self.serializer_class(data = data)
#         email = request.data['email']
#         if Candidate.objects.filter(email = email).exists():
#             user = Candidate.objects.get(email = email)
#             uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
#             token = PasswordResetTokenGenerator().make_token(user)
#             current_site = get_current_site(request=request).domain
#             relative_link = reverse('users:candidate-password_reset', kwargs={'uidb64': uidb64, 'token': token})
#             absolute_url = 'http://'+current_site+relative_link
#             email_body= 'Hello, \n Please use the link below to reset your password \n'+ absolute_url
#             data={'email_body': email_body, 'email_subject': 'Reset your password', 'to_email': user.email}
#             Util.send_email(data)
#         return Response({'success': 'A link was sent to your email to reset your password'}, status=status.HTTP_200_OK)


# class CandidatePasswordTokenConfirmView(GenericAPIView):
#     serializer_class = CandidatePasswordTokenConfirmSerializer
#     # def get_serializer_class(self):
#     #     return None
    
#     # @swagger_auto_schema(auto_schema=False)
#     def get(self, request, uidb64, token):
        
#         try:
#             id = smart_str(urlsafe_base64_decode(uidb64))
#             user = Candidate.objects.get(id=id)

#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'})
#             return Response({'sucess': True, 'message': 'Credentials are valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

#         except DjangoUnicodeDecodeError as identifier:
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({'error': 'Token is not valid, please request a new one'})

# class CandidateSetNewPasswordView(GenericAPIView):
#     serializer_class = CandidateSetNewPasswordSerializer

#     def patch(self, request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         return Response({'success': True, 'message': 'Password reset successfully'}, status=status.HTTP_200_OK)

# class CandidateLogOutView(GenericAPIView):
#     serializer_class = CandidateLogOutSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# # 