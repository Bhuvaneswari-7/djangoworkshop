# Generated by Django 5.0.3 on 2024-03-28 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_data_student_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student_data',
            new_name='student_student_data',
        ),
    ]
