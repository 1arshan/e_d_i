from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Institute, InstituteTeacher, Class, Assignment


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ['name', 'pincode', 'address', 'is_verified', 'pk']


class InstituteAssosiatedSerializer(serializers.ModelSerializer):
    administrative_right = serializers.BooleanField()

    class Meta:
        model = Institute
        fields = ['name', 'pincode', 'address', 'is_verified', 'id', 'administrative_right']


class InstituteTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteTeacher
        fields = ['teacher_link', 'institute_link', 'administrative_right', 'pk']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['code', 'name', 'teacher_link', 'institute_link', 'description', 'pk', 'standard_or_class']


class AssingmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['class_link', 'given_datetime', 'end_datetime', 'file', 'description', 'pk']
