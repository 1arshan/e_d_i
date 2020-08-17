from .models import AssignmentSubmission
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

"""
@receiver(post_save, sender=AssignmentSubmission)
def ass_submission_signal(sender,instance, **kwargs):
    
"""