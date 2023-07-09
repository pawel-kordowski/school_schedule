from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Student(models.Model):
    name = models.CharField(max_length=256)
    klass = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students")


class Teacher(models.Model):
    name = models.CharField(max_length=256)


class Subject(models.Model):
    name = models.CharField(max_length=256)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Schedule(models.Model):
    klass = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField()
    hour = models.PositiveSmallIntegerField()
