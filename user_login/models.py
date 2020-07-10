from django.db import models
from subject_material.models import VideoMaterial


# ------------doubts question ------->>>>>>>
def renaming_uploaded_file1(instance, filename):
    return "doubts_question/" + str(instance.pk) + "_" + filename


class DoubtsQuestion(models.Model):
    material_link = models.ForeignKey(VideoMaterial, on_delete=models.CASCADE)
    doubts_question = models.TextField()
    is_answered = models.BooleanField(default=False)


class DoubtsQuestionPhotos(models.Model):
    doubts_question_link = models.ForeignKey(DoubtsQuestion, on_delete=models.CASCADE,
                                             related_name='question_doubts_link')
    image = models.ImageField(blank=True, upload_to=renaming_uploaded_file1)


class QuestionComment(models.Model):
    comment_question_link = models.ForeignKey(DoubtsQuestion, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)


# ----doubts answer ----------.>>>>>
def renaming_uploaded_file2(instance, filename):
    return "doubts_answer/" + str(instance.pk) + "_" + filename


class DoubtsAnswer(models.Model):
    answer_question_link = models.ForeignKey(DoubtsQuestion, on_delete=models.CASCADE)
    doubts_answer = models.TextField()


class DoubtsAnswerPhotos(models.Model):
    doubts_answer_link = models.ForeignKey(DoubtsAnswer, on_delete=models.CASCADE,
                                           related_name='answer_doubts_link')
    image = models.ImageField(blank=True, upload_to=renaming_uploaded_file2)


class AnswerComment(models.Model):
    comment_answer_link = models.ForeignKey(DoubtsAnswer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
