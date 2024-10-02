import pytest
from rest_framework import status
from django.urls import reverse
from main.models import Team, Person


@pytest.mark.django_db
class TestTeamViewSet:
    def test_create_team(self, client):
        response = client.post(reverse('team-list'), {'name': 'Team C'})
        assert response.status_code == status.HTTP_201_CREATED
        assert Team.objects.count() == 1

    def test_list_teams(self, client, team):
        response = client.get(reverse('team-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_patch_team(self, client, team):
        response = client.patch(
            reverse('team-detail', args=[team.id]),
            {'name': 'Updated Team A'},
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_200_OK
        team.refresh_from_db()
        assert team.name == 'Updated Team A'

    def test_delete_team(self, client, team):
        response = client.delete(reverse('team-detail', args=[team.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Team.objects.count() == 0


@pytest.mark.django_db
class TestPersonViewSet:
    def test_create_person(self, client):
        response = client.post(reverse('person-list'), {
            'first_name': 'Alice',
            'last_name': 'Smith',
            'email': 'alice.smith@example.com'
        })
        assert response.status_code == status.HTTP_201_CREATED
        assert Person.objects.count() == 1

    def test_list_people(self, client, person, another_person):
        response = client.get(reverse('person-list'))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_patch_person(self, client, person):
        response = client.patch(
            reverse('person-detail', args=[person.id]),
            {'first_name': 'Updated Name'},
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_200_OK
        person.refresh_from_db()
        assert person.first_name == 'Updated Name'

    def test_delete_person(self, client, person):
        response = client.delete(reverse('person-detail', args=[person.id]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Person.objects.count() == 0


@pytest.mark.django_db
class TestAddPersonToTeamAPIView:
    def test_add_person_to_team(self, client, team, person):
        response = client.post(
            reverse('person-add-to-team', args=[person.id]),
            {'team_id': team.id}
        )
        assert response.status_code == status.HTTP_200_OK
        assert team in person.teams.all()

    def test_add_person_to_nonexistent_team(self, client, person):
        response = client.post(
            reverse('person-add-to-team', args=[person.id]),
            {'team_id': 999}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestRemovePersonFromTeamAPIView:
    def test_remove_person_from_team(self, client, team, person):
        person.teams.add(team)
        response = client.post(
            reverse('person-remove-from-team', args=[person.id]),
            {'team_id': team.id}
        )
        assert response.status_code == status.HTTP_200_OK
        assert team not in person.teams.all()

    def test_remove_person_from_nonexistent_team(self, client, person):
        response = client.post(
            reverse('person-remove-from-team', args=[person.id]),
            {'team_id': 999}
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
