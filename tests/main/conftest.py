import pytest
from main.models import Team, Person


@pytest.fixture
def team():
    return Team.objects.create(name="Team A")


@pytest.fixture
def person():
    return Person.objects.create(first_name="John", last_name="Doe", email="john.doe@example.com")


@pytest.fixture
def another_person():
    return Person.objects.create(first_name="Jane", last_name="Doe", email="jane.doe@example.com")
