# Generated by Django 3.0.8 on 2020-07-09 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_material', '0003_notesmaterial_testing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notesmaterial',
            name='testing',
        ),
    ]
