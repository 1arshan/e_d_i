# Generated by Django 3.0.8 on 2020-08-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0017_assignmentsubmission_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentattach',
            name='student_name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
