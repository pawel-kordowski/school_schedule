from rest_framework.serializers import ModelSerializer, IntegerField

from schedule.models import Schedule, Class, Subject


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

    def get_fields(self):
        return super().get_fields() | {"class": ClassSerializer(source="klass")}

    class Meta:
        model = Schedule
        fields = ["day_of_week", "hour", "subject"]
