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
