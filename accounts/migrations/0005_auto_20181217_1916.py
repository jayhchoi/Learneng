# Generated by Django 2.1.4 on 2018-12-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181213_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default/profile-default.jpg', upload_to='%Y/%m/%d/profile/', verbose_name='프로필 사진'),
        ),
    ]