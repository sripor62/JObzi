# Generated by Django 3.2.5 on 2022-02-27 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0003_application_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Company',
        ),
    ]