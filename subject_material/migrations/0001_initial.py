# Generated by Django 3.0.8 on 2020-07-13 13:07

from django.db import migrations, models
import django.db.models.deletion
import subject_material.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardOrClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_or_class', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('video_link', models.URLField(blank=True)),
                ('teacher_name', models.CharField(default='Anonymous', max_length=50)),
                ('standard_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_material.StandardOrClass', to_field='standard_or_class')),
                ('subject_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_material.Subject', to_field='subject_name')),
                ('teacher_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_signup.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NotesMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.FileField(blank=True, upload_to=subject_material.models.renaming_uploaded_file1)),
                ('question_ans', models.FileField(blank=True, upload_to=subject_material.models.renaming_uploaded_file2)),
                ('notes_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes_material_link', to='subject_material.VideoMaterial')),
            ],
        ),
    ]
