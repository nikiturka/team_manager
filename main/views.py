from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer, TeamMembershipSerializer
from django.shortcuts import get_object_or_404


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TeamMembershipViewSet(viewsets.ViewSet):
    """
    A ViewSet for managing team membership.

    This ViewSet provides the following actions:
    - add_member: Adds a person to a specified team.
        Requires 'team_id' to be passed in the request body.
    - remove_member: Removes a person from a specified team.
        Requires 'team_id' to be passed in the request body.
    """
    def add_member(self, request, pk):
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
