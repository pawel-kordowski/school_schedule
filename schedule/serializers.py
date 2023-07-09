from rest_framework.serializers import ModelSerializer, IntegerField

from schedule.models import Schedule, Class


class ClassSerializer(ModelSerializer):
    student_count = IntegerField()

    class Meta:
        model = Class
        fields = ["name", "student_count"]


class ScheduleSerializer(ModelSerializer):
    def get_fields(self):
        return super().get_fields() | {"class": ClassSerializer(source="klass")}

    class Meta:
        model = Schedule
        fields = ["day_of_week", "hour"]
