# Generated by Django 2.2.15 on 2020-08-31 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_education_info_skills_voluneering_work'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='voluneering',
            new_name='hobby',
        ),
    ]
