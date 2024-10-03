from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer, TeamMembershipSerializer
from django.shortcuts import get_object_or_404


# CRUD for Teams
class TeamViewSet(viewsets.ModelViewSet):
    """
    General ViewSet description

    list: Retrieve a list of all available teams.

    retrieve: Retrieve the details of a specific team by its ID.

    create: Create a new team with the specified attributes such as name, description, etc.

    update: Update the information of an existing team by its ID.

    partial_update: Partially update a team (only the provided attributes will be updated).

    destroy: Delete a team by its ID.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# CRUD for Persons
class PersonViewSet(viewsets.ModelViewSet):
    """
    General ViewSet description

    list: Retrieve a list of all available persons.

    retrieve: Retrieve the details of a specific person by their ID.

    create: Create a new person with the specified attributes like name, age, etc.

    update: Update the information of an existing person by their ID.

    partial_update: Partially update a person's details (only the provided attributes will be updated).

    destroy: Delete a person by their ID.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# A ViewSet for adding or removing members from a team.
class TeamMembershipViewSet(viewsets.ViewSet):
    """
    General ViewSet description

    add_member: Add a person to a team.
    remove_member: Remove a person from a team.

    The request body should contain:
    - team_id: The ID of the team to which the person is being added or from which the person is being removed.
    """
    def add_member(self, request, pk):
        """
        Add a person to a team.

        Args:
        - request: The HTTP request containing the team information (team_id).
        - pk: The ID of the person to be added to the team.

        The request body should contain:
        - team_id: The ID of the team.

        Returns:
        - HTTP 200 OK if the person was successfully added to the team.
        - HTTP 400 BAD REQUEST if the person is already a member of the team or if the data is invalid.
        """
        person = get_object_or_404(Person, id=pk)
        serializer = TeamMembershipSerializer(data=request.data)

        if serializer.is_valid():
            team_id = serializer.validated_data['team_id']
            team = get_object_or_404(Team, id=team_id)

            if person.teams.filter(id=team.id).exists():
                return Response({'status': 'person is already in this team'}, status=status.HTTP_400_BAD_REQUEST)

            person.teams.add(team)
            return Response({'status': 'person added to team'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def remove_member(self, request, pk):
        """
        Remove a person from a team.

        Args:
        - request: The HTTP request containing the team information (team_id).
        - pk: The ID of the person to be removed from the team.

        The request body should contain:
        - team_id: The ID of the team.

        Returns:
        - HTTP 200 OK if the person was successfully removed from the team.
        - HTTP 400 BAD REQUEST if the person is not a member of the team or if the data is invalid.
        """
        person = get_object_or_404(Person, id=pk)
        serializer = TeamMembershipSerializer(data=request.data)

        if serializer.is_valid():
            team_id = serializer.validated_data['team_id']
            team = get_object_or_404(Team, id=team_id)

            if not person.teams.filter(id=team.id).exists():
                return Response({'status': 'person is not in this team'}, status=status.HTTP_400_BAD_REQUEST)

            person.teams.remove(team)
            return Response({'status': 'person removed from team'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
