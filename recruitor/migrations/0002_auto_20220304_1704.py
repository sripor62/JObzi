# Generated by Django 3.2.5 on 2022-03-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='looking_for',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]