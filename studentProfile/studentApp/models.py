from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    parents_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    behavior_and_social_skills = models.TextField()
    interests_and_extracurricular = models.TextField()
    motivation_and_engagement = models.TextField()
    special_needs = models.TextField()
    unhealthy_habits = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    grade_sheet = models.FileField(upload_to='gradesheets/')

    def __str__(self):
        return self.name
