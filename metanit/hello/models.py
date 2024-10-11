from django.db import models
 
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self) -> str:
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=30)
 
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    def __str__(self) -> str:
        return f'{self.name} {self.price},- {self.company.name}'
    
class Course(models.Model):
    name = models.CharField(max_length=30)
    students = models.ManyToManyField('Student', through="Enrollment")
    def __str__(self) -> str:
        return f'{self.name}'
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField('Course', through="Enrollment")
    def __str__(self) -> str:
        return f'{self.name}'
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()   # дата поступления
    mark = models.IntegerField()  # полученный балл
    def __str__(self) -> str:
        return f'{self.student.id}.{self.student.name}-{self.course.id}.{self.course.name} {self.date} {self.mark}'
    