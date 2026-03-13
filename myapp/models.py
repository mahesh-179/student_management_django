from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    gpa = models.FloatField()
    final_grade = models.CharField(max_length=3)

    def __str__(self):
       return self.name

class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='students/')
    dob = models.DateField()
    address = models.TextField()
    joining_date = models.DateField()

    def __str__(self):
        return self.student.name





