# Generated by Django 3.0.8 on 2020-08-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_auto_20200811_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='name',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]
