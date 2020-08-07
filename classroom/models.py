from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=60)
    pincode = models.CharField(max_length=10)
    address = models.TextField()


class InstituteTeacher(models.Model):
    pass
