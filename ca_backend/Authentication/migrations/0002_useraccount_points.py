# Generated by Django 4.2.6 on 2023-10-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
