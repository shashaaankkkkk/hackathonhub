# Generated by Django 3.2.13 on 2024-01-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20240120_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='channel_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]