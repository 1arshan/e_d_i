# Generated by Django 3.0.8 on 2020-08-23 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields
import user_signup.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TempStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('pincode', models.CharField(max_length=10)),
                ('standard_or_class', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
                ('course_field', models.CharField(blank=True, default='no_field', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TempTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True)),
                ('password', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
                ('subject', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), blank=True, size=None)),
                ('max_qualification', models.CharField(max_length=50)),
                ('experience', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TestingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='testing1')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('photo', models.ImageField(blank=True, upload_to=user_signup.models.renaming_uploaded_file1)),
                ('teacher_description', models.TextField(blank=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
                ('is_verified', models.BooleanField(default=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True)),
                ('subject', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), blank=True, size=None)),
                ('max_qualification', models.CharField(max_length=50)),
                ('experience', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('photo', models.ImageField(blank=True, upload_to=user_signup.models.renaming_uploaded_file1)),
                ('standard_or_class', models.CharField(max_length=10)),
                ('email_verified', models.BooleanField(default=False)),
                ('pincode', models.CharField(max_length=12)),
                ('date', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=8)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(max_length=13, primary_key=True, serialize=False, unique=True)),
                ('course_field', models.CharField(blank=True, default='no_field', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
