# Generated by Django 5.1.4 on 2024-12-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_industryentry_path_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='industryentry',
            name='entry_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
