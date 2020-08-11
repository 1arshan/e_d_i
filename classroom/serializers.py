from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Institute, InstituteTeacher, Class


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ['name', 'pincode', 'address', 'is_verified', 'pk']


class InstituteTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteTeacher
        fields = ['teacher_link', 'institute_link', 'administrative_right', 'pk']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['code', 'name', 'teacher_link', 'institute_link', 'description', 'pk']
