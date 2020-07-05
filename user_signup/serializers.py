from .models import TempStudent, TempTeacher
from rest_framework import serializers


class TempStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempStudent
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'standard_or_class'
            , 'pincode']


class TempTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempTeacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password'
            , 'description']
