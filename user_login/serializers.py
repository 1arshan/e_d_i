from rest_framework import serializers
from subject_material.models import VideoMaterial, NotesMaterial
from .models import DoubtsQuestion, QuestionComment, DoubtsQuestionPhotos, \
    DoubtsAnswer, DoubtsAnswerPhotos, AnswerComment
from user_signup.models import TeacherProfile


class NotesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesMaterial
        fields = ['notes_link', 'notes', 'question_ans', 'id']


# -----home page------------->>>>>>>>Student
class StudentHomePageSerializer(serializers.ModelSerializer):
    notes_material_link = NotesMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = VideoMaterial
        fields = ['subject_link', 'standard_link', 'topic', 'description', 'video_link',
                  'notes_material_link', 'teacher_name', 'pk']

    def create(self, validated_data):
        notes_material_data = validated_data.pop('notes_material_link')
        temp = VideoMaterial.objects.create(**validated_data)
        for x in notes_material_data:
            NotesMaterial.objects.create(notes_link=temp, **x)
        return temp


# -------subject view --------->>>>>>>
class SubjectViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoMaterial
        fields = ['chapter']


# -------chapter view --------->>>>>>>
class ChapterSerializer(serializers.ModelSerializer):
    notes_material_link = NotesMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = VideoMaterial
        fields = ['chapter', 'topic','notes_material_link','description', 'video_link', 'teacher_link', 'teacher_name', 'thumbnail']


# -------home page teacher------->>>>
class TeacherHomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['subject']


# -------doubts part started----------->>>>
class DoubtsQuestionPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubtsQuestionPhotos
        fields = ['image']


class DoubtsQuestionCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionComment
        fields = ['comment']


# when only question ,comment and photo are seen
class DoubtsQuestionSerializer(serializers.ModelSerializer):
    question_photos_link = DoubtsQuestionPhotosSerializer(many=True)
    question_comment_link = DoubtsQuestionCommentSerializer(many=True)

    class Meta:
        model = DoubtsQuestion
        fields = ['question_photos_link', 'material_link', 'doubts_question', 'pk', 'question_comment_link'
            , 'teacher_link']


# -----doubts answer serializer--------->>>>>>>
class DoubtsAnswerPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoubtsAnswerPhotos
        fields = ['image']


class DoubtsAnswerSerializer(serializers.ModelSerializer):
    answer_doubts_link = DoubtsQuestionPhotosSerializer(many=True)

    class Meta:
        model = DoubtsAnswer
        fields = ['answer_question_link', 'doubts_answer', 'pk'
            , 'answer_doubts_link']


# question along with photo,anser .comment are seen
class DoubtsQuestionAnswerSerializer(serializers.ModelSerializer):
    question_doubts_link = DoubtsQuestionPhotosSerializer(many=True)
    question_comment_link = DoubtsQuestionCommentSerializer(many=True)

    class Meta:
        model = DoubtsQuestion
        fields = ['material_link', 'doubts_question', 'pk', 'question_comment_link'
            , 'question_photos_link']
