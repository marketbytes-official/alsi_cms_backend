# Generated by Django 5.1.4 on 2024-12-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_rename_industry_title_industryentry_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='industryentry',
            old_name='title',
            new_name='industries_title',
        ),
        migrations.RemoveField(
            model_name='industryentry',
            name='description',
        ),
        migrations.AddField(
            model_name='industryentry',
            name='industries_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
