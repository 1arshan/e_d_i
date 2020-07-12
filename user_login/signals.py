from .models import QuestionComment, DoubtsQuestion, DoubtsAnswer
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=QuestionComment)
def question_comment(sender, instance, **kwargs):
    t = instance.question_link_comment
    t.is_answered = False
    t.save()


@receiver(pre_save, sender=DoubtsQuestion)
def question_doubts(sender, instance, **kwargs):
    instance.teacher_link = instance.material_link.teacher_link


@receiver(pre_save, sender=DoubtsAnswer)
def answer_given(sender, instance, **kwargs):
    t = instance.answer_question_link
    t.is_answered = True
    t.save()
