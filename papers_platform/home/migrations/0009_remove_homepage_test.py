# Generated by Django 2.0.7 on 2018-07-20 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='test',
        ),
    ]