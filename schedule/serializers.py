from rest_framework.serializers import ModelSerializer, IntegerField

from schedule.models import Schedule, Class, Subject, Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name"]


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ["name"]


class ClassSerializer(ModelSerializer):
    student_count = IntegerField()

    class Meta:
        model = Class
        fields = ["name", "student_count"]


class ScheduleSerializer(ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer(source="subject.teacher")

    def get_fields(self):
        return super().get_fields() | {"class": ClassSerializer(source="klass")}

    class Meta:
        model = Schedule
        fields = ["day_of_week", "hour", "subject", "teacher"]
