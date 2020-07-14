from .models import TempStudent, TempTeacher, StudentProfile, TeacherProfile
from rest_framework import serializers


class TempStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempStudent
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'standard_or_class'
            , 'pincode', 'course_field']


class TempTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempTeacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password'
            , 'description', 'subject', 'max_qualification', 'experience']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['photo', 'first_name', 'last_name', 'email', 'phone_number', 'standard_or_class'
            , 'pincode', 'email_verified', 'course_field']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['photo', 'first_name', 'last_name', 'email', 'phone_number', 'teacher_description'
            , 'email_verified', 'subject', 'max_qualification', 'experience']
