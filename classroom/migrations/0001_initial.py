# Generated by Django 3.0.8 on 2020-08-25 18:44

import classroom.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_datetime', models.DateTimeField(auto_now_add=True)),
                ('end_datetime', models.DateTimeField()),
                ('file', models.FileField(upload_to=classroom.models.renaming_uploaded_file1)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('standard_or_class', models.CharField(default='null', max_length=10)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('name', models.CharField(max_length=20)),
                ('teacher_name', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('pincode', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('is_verified', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=25)),
                ('class_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Class')),
                ('student_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_signup.StudentProfile')),
            ],
        ),
        migrations.CreateModel(
            name='InstituteTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrative_right', models.BooleanField(default=False)),
                ('teacher_name', models.CharField(blank=True, max_length=25)),
                ('institute_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Institute')),
                ('teacher_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_signup.TeacherProfile')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='institute_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Institute'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user_signup.TeacherProfile'),
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_datetime', models.DateTimeField(auto_now_add=True)),
                ('time_remark', models.BooleanField(default=False)),
                ('ans_file', models.FileField(upload_to=classroom.models.renaming_uploaded_file2)),
                ('student_name', models.CharField(blank=True, max_length=25)),
                ('assignment_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Assignment')),
                ('student_link', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user_signup.StudentProfile')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='class_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Class'),
        ),
    ]
