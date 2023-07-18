from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Recruiter, Candidate
from django.contrib import auth

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
        
        return super().validate(attrs)