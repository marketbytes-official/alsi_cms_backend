# Generated by Django 5.1.4 on 2024-12-20 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_industry_industryentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='industryentry',
            old_name='industry_title',
            new_name='title',
        ),
    ]
