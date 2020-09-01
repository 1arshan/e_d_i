from django.db import models
from user_signup.models import TeacherProfile, StudentProfile
from subject_material.models import StandardOrClass, Subject
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.auth.models import User


class Institute(models.Model):
    name = models.CharField(max_length=60)
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class InstituteTeacher(models.Model):
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    institute_link = models.ForeignKey(Institute, on_delete=models.CASCADE)
    administrative_right = models.BooleanField(default=False)
    teacher_name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'Teacher: {self.teacher_link}; Institute: {self.institute_link}'


class Class(models.Model):
    code = models.CharField(max_length=10, unique=True)
    standard_or_class = models.CharField(max_length=10, default="null")
    # = models.CharField(max_length=30)
    teacher_link = models.ForeignKey(TeacherProfile, on_delete=models.DO_NOTHING)
    institute_link = models.ForeignKey(Institute, on_delete=models.CASCADE)
    description = models.CharField(max_length=256, blank=True)
    name = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'Class Code :{self.code} Teacher name: {self.teacher_name}'


def renaming_uploaded_file1(instance, filename):
    return "institute/" + str(instance.class_link) + "/assignment/" + filename


def renaming_uploaded_file2(instance, filename):
    return "institute/" + str(instance.assignment_link.class_link) + "/assignment_submitted/" + filename


class Assignment(models.Model):
    class_link = models.ForeignKey(Class, on_delete=models.CASCADE, to_field='id')
    given_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField()
    file = models.FileField(upload_to=renaming_uploaded_file1)
    description = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f'Assignmnet link:{str(self.pk)} ; class link:{self.class_link}'


class StudentAttach(models.Model):
    class_link = models.ForeignKey(Class, on_delete=models.CASCADE, to_field='id')
    student_link = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return str(self.class_link)


class AssignmentSubmission(models.Model):
    assignment_link = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission_datetime = models.DateTimeField(auto_now_add=True)
    time_remark = models.BooleanField(default=False)  # if on time then True
    ans_file = models.FileField(upload_to=renaming_uploaded_file2)
    student_link = models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING)
    student_name = models.CharField(max_length=25, blank=True)


def renaming_uploaded_file3(instance, filename):
    return "questionbank/" + str(instance.subject_link.class_link) + "/" + str(instance.subject_link.subject) + \
           "/" + str(instance.chapter) + "/question_" + filename


def renaming_uploaded_file4(instance, filename):
    return "questionbank/" + str(instance.subject_link.class_link) + "/" + str(instance.subject_link.subject) + \
           "/" + str(instance.chapter) + "/answer_" + filename


# ------Mock test Begin


class QuestionBank(models.Model):
    class_link = models.ForeignKey(StandardOrClass, on_delete=models.CASCADE, to_field='standard_or_class')
    subject_link = models.ForeignKey(Subject, on_delete=models.CASCADE, to_field='subject_name')
    chapter = models.CharField(max_length=30)
    question = models.TextField()
    option = ArrayField(models.CharField(max_length=20, blank=True), blank=True)
    answer = models.CharField(max_length=2)
    ques_photo = models.ImageField(blank=True, upload_to=renaming_uploaded_file3)
    ans_photo = models.ImageField(blank=True, upload_to=renaming_uploaded_file4)
    explanation = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    public_access = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.pk}'


class StudentTest(models.Model):
    type = models.CharField(max_length=10)
    student_link = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    total_mark = models.CharField(max_length=5)
    mark_score = models.CharField(max_length=5)
    date = models.DateTimeField()
    class_link = models.ForeignKey(Class, on_delete=models.DO_NOTHING, blank=True, null=True)
    visibility = models.BooleanField(default=False)


class StudentTestData(models.Model):
    ques_pk = models.ForeignKey(QuestionBank, on_delete=models.CASCADE, related_name='pk_ques')
    option_selected = models.CharField(max_length=2)
    student_test_link = models.ForeignKey(StudentTest, on_delete=models.DO_NOTHING, related_name='student_link_test',
                                          blank=True)


class ClassTest(models.Model):
    class_link = models.ForeignKey(Class, on_delete=models.CASCADE)
    mark_per_ques = models.CharField(max_length=5)
    negative_marking = models.CharField(max_length=3)
    starting_time = models.DateTimeField()
    ending_time = models.DateTimeField(blank=True)
    visibility = models.BooleanField(default=False)


class ClassTestQuestion(models.Model):
    class_test_link = models.ForeignKey(ClassTest, on_delete=models.CASCADE, related_name='class_link_test', blank=True)
    ques_pk = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
