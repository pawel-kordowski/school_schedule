from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
