# Generated by Django 5.1.4 on 2025-01-05 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss_app', '0007_news_guid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='guid',
        ),
    ]