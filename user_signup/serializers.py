from .models import TempStudent, TempTeacher, StudentProfile, TeacherProfile, TestingModel
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from subject_material.models import VideoMaterial


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
    photo = Base64ImageField()

    class Meta:
        model = StudentProfile
        fields = ['photo', 'first_name', 'last_name', 'email', 'phone_number', 'standard_or_class'
            , 'pincode', 'email_verified', 'course_field']

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.standard_or_class = validated_data.get('standard_or_class', instance.standard_or_class)
        instance.pincode = validated_data.get('pincode', instance.pincode)
        instance.email_verified = validated_data.get('email_verified', instance.email_verified)
        instance.course_field = validated_data.get('course_field', instance.course_field)
        instance.save()
        return instance


class TeacherSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

    class Meta:
        model = TeacherProfile
        fields = ['photo', 'first_name', 'last_name', 'email', 'phone_number', 'teacher_description'
            , 'email_verified', 'subject', 'max_qualification', 'experience']

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.teacher_description = validated_data.get('teacher_description', instance.teacher_description)
        instance.email_verified = validated_data.get('email_verified', instance.email_verified)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.max_qualification = validated_data.get('max_qualification', instance.max_qualification)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.save()
        return instance


class TestingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link',
                  'chapter', 'teacher_link']
