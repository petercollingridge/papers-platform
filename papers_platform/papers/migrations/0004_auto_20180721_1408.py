# Generated by Django 2.0.7 on 2018-07-21 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_paperpage_video_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paperpage',
            old_name='intro',
            new_name='summary',
        ),
    ]