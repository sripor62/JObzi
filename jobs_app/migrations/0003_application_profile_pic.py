# Generated by Django 3.2.5 on 2022-02-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]