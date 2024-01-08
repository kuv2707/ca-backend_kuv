# Generated by Django 3.2.12 on 2023-12-21 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_tasksubmission_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksubmission',
            name='admin_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasksubmission',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 22, 23, 18, 757893), help_text='Deadline for the Task'),
        ),
    ]
