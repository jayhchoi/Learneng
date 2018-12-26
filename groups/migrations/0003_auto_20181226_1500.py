# Generated by Django 2.1.4 on 2018-12-26 06:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20181219_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='group',
            name='size',
            field=models.PositiveSmallIntegerField(default=4, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(1)], verbose_name='최대정원'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
