from rest_framework import serializers
from .models import User, Recruiter, Candidate

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