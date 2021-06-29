from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Direction(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    direction = models.ForeignKey(Direction, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Group(models.Model):
    number = models.SmallIntegerField()
    direction = models.ForeignKey(Direction, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.number}'

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'