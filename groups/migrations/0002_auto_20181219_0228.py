# Generated by Django 2.1.4 on 2018-12-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('closed', 'Closed'), ('full', 'Full')], default='open', max_length=40),
        ),
    ]
