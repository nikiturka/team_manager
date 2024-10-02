from rest_framework import serializers
from .models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class TeamMembershipSerializer(serializers.Serializer):
    team_id = serializers.IntegerField(required=True)
