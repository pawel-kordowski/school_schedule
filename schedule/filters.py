from django_filters.rest_framework import FilterSet, CharFilter


class ScheduleFilter(FilterSet):
    class_name = CharFilter("klass__name")
