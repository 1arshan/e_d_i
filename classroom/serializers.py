from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Institute, InstituteTeacher, Class, Assignment, AssignmentSubmission, StudentAttach, QuestionBank, \
    StudentTest, StudentTestData, ClassTest, ClassTestQuestion


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


class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = ['class_link', 'subject_link', 'chapter', 'question', 'option', 'answer', 'ques_photo', 'ans_photo',
                  'explanation', 'pk', 'created_by']


class QuesBankStudnentResuktSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionBank
        fields = ['subject_link', 'chapter', 'question', 'option', 'answer', 'ques_photo', 'ans_photo',
                  'explanation', 'pk']


class StudentResultDataGetSerializer(serializers.ModelSerializer):
    ques_pk = QuestionBankSerializer()

    class Meta:
        model = StudentTestData
        fields = ['ques_pk', 'option_selected', 'student_test_link']


class StudentResultDataPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTestData
        fields = ['ques_pk', 'option_selected', 'student_test_link']


class StudentResultGetSerializer(serializers.ModelSerializer):
    student_link_test = StudentResultDataGetSerializer(many=True)

    class Meta:
        model = StudentTest
        fields = ['total_mark', 'type', 'mark_score', 'student_link_test', 'id', 'date', 'student_link', 'class_link']


class StudentResultPostSerializer(serializers.ModelSerializer):
    student_link_test = StudentResultDataPostSerializer(many=True)

    class Meta:
        model = StudentTest
        fields = ['total_mark', 'type', 'mark_score', 'student_link_test', 'id', 'date', 'student_link', 'class_link']

    def create(self, validated_data):
        student_link_test_data = validated_data.pop('student_link_test')

        temp = StudentTest.objects.create(**validated_data)
        for x in student_link_test_data:
            StudentTestData.objects.create(student_test_link=temp, **x)
        return temp


# ----need to create a update
class ClassTestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTestQuestion
        fields = ['ques_pk', 'pk']

#for teacher to post delete ques paper
class ClassTestSerializer(serializers.ModelSerializer):
    class_link_test = ClassTestQuestionSerializer(many=True)

    class Meta:
        model = ClassTest
        fields = ['class_link', 'mark_per_ques', 'negative_marking', 'starting_time', 'class_link_test',
                  'ending_time', 'pk']

    def create(self, validated_data):
        class_link_test_data = validated_data.pop('class_link_test')

        temp = ClassTest.objects.create(**validated_data)
        for x in class_link_test_data:
            ClassTestQuestion.objects.create(class_test_link=temp, **x)
        return temp


#---For teacher to see ques paper
class ClassTestQuestionGetSerializer(serializers.ModelSerializer):
    ques_pk = QuestionBankSerializer()
    class Meta:
        model = ClassTestQuestion
        fields = ['ques_pk', 'pk']




class ClassTestGetSerializer(serializers.ModelSerializer):
    class_link_test = ClassTestQuestionGetSerializer(many=True)

    class Meta:
        model = ClassTest
        fields = ['class_link', 'mark_per_ques', 'negative_marking', 'starting_time', 'class_link_test',
                  'ending_time', 'pk']




# For student to see their due test in class
class ClassTestQuestionStudentSerializer(serializers.ModelSerializer):
    ques_pk = QuestionBankSerializer()

    class Meta:
        model = ClassTestQuestion
        fields = ['ques_pk', 'pk']


class ClassTestStudentSerializer(serializers.ModelSerializer):
    class_link_test = ClassTestQuestionStudentSerializer(many=True)

    class Meta:
        model = ClassTest
        fields = ['class_link', 'mark_per_ques', 'negative_marking', 'starting_time', 'class_link_test',
                  'ending_time', 'pk']
