from rest_framework import viewsets, status
from rest_framework.views import APIView
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


class AddPersonToTeamAPIView(APIView):
    def post(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        serializer = TeamMembershipSerializer(data=request.data)

        if serializer.is_valid():
            team_id = serializer.validated_data['team_id']
            team = get_object_or_404(Team, id=team_id)

            person.teams.add(team)
            return Response({'status': 'person added to team'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemovePersonFromTeamAPIView(APIView):
    def post(self, request, pk):
        person = get_object_or_404(Person, id=pk)
        serializer = TeamMembershipSerializer(data=request.data)

        if serializer.is_valid():
            team_id = serializer.validated_data['team_id']
            team = get_object_or_404(Team, id=team_id)

            person.teams.remove(team)
            return Response({'status': 'person removed from team'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
