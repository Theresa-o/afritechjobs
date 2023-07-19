from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Recruiter, Candidate
from django.contrib import auth

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework_simplejwt.tokens import RefreshToken, TokenError




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
# ensure that email can be used
# ensure that username is between 6 to 12 and it shouldn't accept numbers
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):

        return User.objects.create_user(**validated_data)
    
class RecruiterRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = Recruiter
        fields = ('email', 'username', 'password')

    def validate(self, attrs):
        # email = attrs.get('email', '')
        # username = attrs.get('username', '')

# ensure that username is between 6 to 12 and it shouldn't accept numbers
        # if not username.isalnum():
        if not attrs['username'].isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):
        return Recruiter.objects.create_user(**validated_data)
    
class CandidateRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = Candidate
        fields = ('email', 'username', 'password')

    def validate(self, attrs):
        # email = attrs.get('email', '')
        # username = attrs.get('username', '')

# ensure that username is between 6 to 12 and it shouldn't accept numbers
        # if not username.isalnum():
        if not attrs['username'].isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):
        return Candidate.objects.create_user(**validated_data)
    
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length = 555)

    class Meta:
        model = User
        fields = ('__all__')

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(max_length=68, min_length=3, read_only=True)
    tokens = serializers.CharField(max_length=68, min_length=3, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        if not user.is_active:
            raise AuthenticationFailed('Account disable, contact admin')
        
        if not user.is_email_verified:
            raise AuthenticationFailed('Email not verified, please verify your email to gain access')
        
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        
    
class RequestPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length = 2)

    class Meta:
        fields = ['email']

# -------------------------------------------
class PasswordTokenConfirmSerializer(serializers.Serializer):
    uidb64 = serializers.CharField(min_length = 1, write_only = True)
    token = serializers.CharField(min_length = 1, write_only = True)

    class Meta:
        fields = ['uidb64', 'token']

    def validate(self, attrs):
        getattr(self, 'swagger_fake_view', False)
        return super().validate(attrs)





# --------------------------------------------

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length = 6, max_length=68, write_only = True)
    uidb64 = serializers.CharField(min_length = 1, write_only = True)
    token = serializers.CharField(min_length = 1, write_only = True)

    class Meta:
        fields = ['password', 'uidb64', 'token']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            uidb64 = attrs.get('uidb64')
            token = attrs.get('token')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid')
            
            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid')
        return super().validate(attrs)

class LogOutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('Bad token')
        