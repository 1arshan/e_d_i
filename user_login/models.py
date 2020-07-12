from django.db import models
from subject_material.models import VideoMaterial
from user_signup.models import TeacherProfile


# ------------doubts question ------->>>>>>>
def renaming_uploaded_file1(instance, filename):
    return "doubts_question/" + str(instance.pk) + "_" + filename


class DoubtsQuestion(models.Model):
    material_link = models.ForeignKey(VideoMaterial, on_delete=models.CASCADE)
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, blank=True)
    doubts_question = models.TextField()
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.doubts_question}'


class DoubtsQuestionPhotos(models.Model):
    question_link_photos = models.ForeignKey(DoubtsQuestion, on_delete=models.CASCADE,
                                             related_name='question_photos_link')
    image = models.ImageField(blank=True, upload_to=renaming_uploaded_file1)


class QuestionComment(models.Model):
    question_link_comment = models.ForeignKey(DoubtsQuestion, on_delete=models.CASCADE,
                                              related_name='question_comment_link')
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
