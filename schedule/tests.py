import pytest
from rest_framework.status import HTTP_200_OK

from schedule.factories import ScheduleFactory, StudentFactory


@pytest.mark.django_db
def test_get_schedule_response_200(client):
    response = client.get("/schedule/")
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_get_schedule_returns_all_items(client):
    ScheduleFactory.create_batch(size=3)
    response = client.get("/schedule/")
    data = response.json()
    assert len(data) == 3


@pytest.mark.django_db
def test_get_schedule_ordered_by_day_of_week_and_hours(client):
    ScheduleFactory(day_of_week=1, hour=1)
    ScheduleFactory(day_of_week=1, hour=0)
    ScheduleFactory(day_of_week=0, hour=0)
    ScheduleFactory(day_of_week=2, hour=0)
    ScheduleFactory(day_of_week=1, hour=2)
    response = client.get("/schedule/")
    data = response.json()
    assert [(d["day_of_week"], d["hour"]) for d in data] == [
        (0, 0),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
    ]


@pytest.mark.django_db
def test_get_schedule_payload(client, django_assert_num_queries):
    schedule_1 = ScheduleFactory(klass__name="5A", day_of_week=0)
    StudentFactory.create_batch(size=3, klass=schedule_1.klass)
    schedule_2 = ScheduleFactory(klass__name="5B", day_of_week=1)
    StudentFactory.create_batch(size=5, klass=schedule_2.klass)
    StudentFactory()
    with django_assert_num_queries(2):
        response = client.get("/schedule/")
    data = response.json()
    assert data == [
        {
            "class": {"name": "5A", "student_count": 3},
            "day_of_week": schedule_1.day_of_week,
            "hour": schedule_1.hour,
        },
        {
            "class": {"name": "5B", "student_count": 5},
            "day_of_week": schedule_2.day_of_week,
            "hour": schedule_2.hour,
        },
    ]
