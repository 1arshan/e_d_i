from .models import QuestionComment, DoubtsQuestion
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=QuestionComment)
def question_comment(sender, instance, **kwargs):
    t = instance.question_link_comment
    t.is_answered = False
    t.save()
