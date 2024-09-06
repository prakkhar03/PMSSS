from rest_framework import serializers
from .models import User, StudentProfile, ScholarshipApplication

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=User.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'user_type']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()

        if user.user_type == 1:
            StudentProfile.objects.create(user=user)
        return user
class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'date_of_birth', 'college_name', 'program', 'year_of_study']
class ScholarshipApplicationSerializer(serializers.ModelSerializer):
    student = StudentProfileSerializer(read_only=True)
    document = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = ScholarshipApplication
        fields = [
            'id',
            'student',
            'application_date',
            'status',
            'scholarship_amount',
            'document',
            'document_status'
        ]
        read_only_fields = ['application_date', 'status', 'document_status']

