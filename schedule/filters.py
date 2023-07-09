from django.utils import timezone
from django_filters.rest_framework import FilterSet, CharFilter, BooleanFilter


class ScheduleFilter(FilterSet):
    class_name = CharFilter("klass__name")
    for_today = BooleanFilter(method="for_today_filter")

    def for_today_filter(self, queryset, name, value):
        if value:
            return queryset.filter(day_of_week=timezone.now().strftime("%w"))

        return queryset
