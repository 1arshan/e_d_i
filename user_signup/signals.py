from django.db.models.signals import pre_save
from django.dispatch import receiver
import random
from broadcaster.sms import broadcast_sms
#from .tasks import send_parallel_sms
from .models import TempTeacher, TempStudent


@receiver(pre_save, sender=TempTeacher)
def teacher_otp(sender, instance, **kwargs):
    instance.otp = random.randrange(10101, 909090)
    print("abc")
    content = "verification code is: " + str(instance.otp) + "\nthis code will valid for only 45 secs"
    #send_parallel_sms.delay(instance.phone_number, content)
    broadcast_sms(instance.phone_number, content)


@receiver(pre_save, sender=TempStudent)
def student_otp(sender, instance, **kwargs):
    instance.otp = random.randrange(10101, 909090)
    content = "verification code is: " + str(instance.otp) + "\nthis code will valid for only 45 secs"
    #send_parallel_sms.delay(instance.phone_number, content)
    broadcast_sms(instance.phone_number, content)