# Generated by Django 5.1.4 on 2024-12-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_blogbanner_title_highlights'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='additional_content',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='main_title',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogentry',
            name='time',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
