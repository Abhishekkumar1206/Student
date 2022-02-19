from django.db import models

# Create your models here.
class Student(models.Model):
    stuNo=models.IntegerField()
    stuName=models.CharField(max_length=100)
    stuId=models.IntegerField()
    stuAddress=models.CharField(max_length=100)