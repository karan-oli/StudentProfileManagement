# Generated by Django 5.0.7 on 2024-07-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parents_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=10)),
                ('roll_no', models.IntegerField()),
                ('behavior_and_social_skills', models.TextField()),
                ('interests_and_extracurricular', models.TextField()),
                ('motivation_and_engagement', models.TextField()),
                ('special_needs', models.TextField()),
                ('unhealthy_habits', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/')),
                ('grade_sheet', models.FileField(upload_to='gradesheets/')),
            ],
        ),
    ]
