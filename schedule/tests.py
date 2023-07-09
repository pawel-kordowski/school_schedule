import pytest
from rest_framework.status import HTTP_200_OK

from schedule.factories import ScheduleFactory


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
