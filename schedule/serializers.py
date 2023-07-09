from rest_framework.serializers import ModelSerializer

from schedule.models import Schedule


class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["day_of_week", "hour"]
