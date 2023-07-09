from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    queryset = Schedule.objects.order_by("day_of_week", "hour")
    serializer_class = ScheduleSerializer
