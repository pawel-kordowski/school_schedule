from django.db.models import Prefetch, Count
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from schedule.models import Schedule, Class
from schedule.serializers import ScheduleSerializer


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    queryset = (
        Schedule.objects.prefetch_related(
            Prefetch(
                "klass",
                queryset=Class.objects.annotate(student_count=Count("students")),
            )
        )
        .select_related("subject__teacher")
        .order_by("day_of_week", "hour")
    )
    serializer_class = ScheduleSerializer
