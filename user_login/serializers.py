from rest_framework import serializers
from subject_material.models import VideoMaterial, NotesMaterial
from .models import DoubtsQuestion, QuestionComment, DoubtsQuestionPhotos, \
    DoubtsAnswer, DoubtsAnswerPhotos, AnswerComment


class NotesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesMaterial
        fields = ['notes', 'question_ans']


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
        fields = ['question_photos_link', 'material_link', 'doubts_question', 'pk', 'question_comment_link']

class DoubtsAnswerSerializer(serializers.ModelSerializer):
    pass


# question along with photo,anser .comment are seen
class DoubtsQuestionAnswerSerializer(serializers.ModelSerializer):
    question_doubts_link = DoubtsQuestionPhotosSerializer(many=True)
    question_comment_link = DoubtsQuestionCommentSerializer(many=True)

    class Meta:
        model = DoubtsQuestion
        fields = ['material_link', 'doubts_question', 'pk', 'question_comment_link'
            , 'question_photos_link']
