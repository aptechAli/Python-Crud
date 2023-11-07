from django.db import models

# Create your models here.


class StudentAddmission(models.Model):
    studentEmail = models.CharField(max_length=200)
    studentName = models.TextField()
    studentCourse = models.TextField()
