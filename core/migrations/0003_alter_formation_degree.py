# Generated by Django 4.2.1 on 2024-06-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_course_image_alter_institution_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='degree',
            field=models.CharField(choices=[('High School', 'High School'), ('Technical', 'Technical'), ('Bachelor', 'Bachelor'), ('Specialization', 'Specialization'), ('Master', 'Master'), ('PhD', 'PhD'), ('Doctorate', 'Doctorate')], max_length=100),
        ),
    ]
