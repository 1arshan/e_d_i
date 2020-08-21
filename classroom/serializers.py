from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Institute, InstituteTeacher, Class, Assignment, AssignmentSubmission, StudentAttach


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
        fields = ['teacher_link', 'institute_link', 'administrative_right', 'teacher_name', 'pk']


class InstituteTeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteTeacher
        fields = ['administrative_right', 'teacher_name']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['code', 'name', 'teacher_name', 'institute_link', 'description', 'pk', 'standard_or_class']


class ClassAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['code', 'name', 'teacher_name', 'teacher_link', 'institute_link', 'description', 'pk',
                  'standard_or_class']


class AssingmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['class_link', 'given_datetime', 'end_datetime', 'file', 'description', 'pk']


class AssingmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['assignment_link', 'submission_datetime', 'time_remark', 'ans_file', 'pk', 'student_link',
                  'student_name']


class StudentAtatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttach
        fields = ['student_link', 'student_name']

class StudentAtatch2Serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttach
        fields = ['student_name']
