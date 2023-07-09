from random import randint

from factory.django import DjangoModelFactory
from factory import Faker, SubFactory, LazyFunction


class ClassFactory(DjangoModelFactory):
    class Meta:
        model = "schedule.Class"

    name = Faker("name")


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = "schedule.Student"

    name = Faker("name")
    klass = SubFactory(ClassFactory)


class TeacherFactory(DjangoModelFactory):
    class Meta:
        model = "schedule.Teacher"

    name = Faker("name")


class SubjectFactory(DjangoModelFactory):
    class Meta:
        model = "schedule.Subject"

    name = Faker("name")
    teacher = SubFactory(TeacherFactory)


class ScheduleFactory(DjangoModelFactory):
    class Meta:
        model = "schedule.Schedule"

    klass = SubFactory(ClassFactory)
    subject = SubFactory(SubjectFactory)
    day_of_week = LazyFunction(lambda: randint(0, 6))
    hour = LazyFunction(lambda: randint(0, 23))
