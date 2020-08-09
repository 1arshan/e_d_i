from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Institute, InstituteTeacher


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ['name', 'pincode', 'address', 'is_verified', 'admin_name']


class InstituteTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteTeacher
        fields = ['teacher_link', 'institute_link', 'administrative_right']
