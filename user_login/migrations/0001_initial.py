# Generated by Django 3.0.8 on 2020-07-14 16:00

from django.db import migrations, models
import django.db.models.deletion
import user_login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject_material', '0001_initial'),
        ('user_signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubtsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubts_answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doubts_question', models.TextField()),
                ('is_answered', models.BooleanField(default=False)),
                ('material_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_material.VideoMaterial')),
                ('teacher_link', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_signup.TeacherProfile')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('question_link_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_comment_link', to='user_login.DoubtsQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsQuestionPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=user_login.models.renaming_uploaded_file1)),
                ('question_link_photos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_photos_link', to='user_login.DoubtsQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='DoubtsAnswerPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=user_login.models.renaming_uploaded_file2)),
                ('doubts_answer_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_doubts_link', to='user_login.DoubtsAnswer')),
            ],
        ),
        migrations.AddField(
            model_name='doubtsanswer',
            name='answer_question_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.DoubtsQuestion'),
        ),
        migrations.CreateModel(
            name='AnswerComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('comment_answer_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_login.DoubtsAnswer')),
            ],
        ),
    ]
