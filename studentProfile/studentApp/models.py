from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, default='0000')
    parents_name = models.CharField(max_length=100)
    behavior = models.TextField(default='')
    social_skills = models.TextField(default='')
    interests = models.TextField(default='')
    engagement_levels = models.TextField(default='')
    special_needs = models.TextField(default='')
    unhealthy_habits = models.TextField(default='')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    grade_sheet = models.FileField(upload_to='grades/', blank=True, null=True)

    def __str__(self):
        return self.name

    def calculate_gpa(self):
        student_subjects = StudentSubject.objects.filter(student=self)
        total_marks = sum(subject.full_marks for subject in student_subjects)
        total_obtained = sum(subject.obtained_marks for subject in student_subjects)
        if total_marks == 0:  # Avoid division by zero
            return 0
        gpa = (total_obtained / total_marks) * 4.0  # Adjust as needed
        return gpa

class Subject(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    full_marks = models.IntegerField()
    obtained_marks = models.IntegerField()