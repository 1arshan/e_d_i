# Generated by Django 3.0.8 on 2020-08-31 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200830_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='classtest',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studenttest',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
    ]
