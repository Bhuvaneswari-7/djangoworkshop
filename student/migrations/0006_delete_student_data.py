# Generated by Django 5.0.3 on 2024-03-28 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_student_data_delete_student_student_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student_data',
        ),
    ]
