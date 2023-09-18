from rest_framework import serializers
from .models import Player, league, state

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ("full_name" ,"age")

class leagueSerializer(serializers.ModelSerializer):
    teams = PlayerSerializer(many=True)  # This includes the player details in the league
    class Meta:
        model = league
        fields = '__all__'

class stateSerializer(serializers.ModelSerializer):
    teams = PlayerSerializer(many=True)  # This includes the player details in the state
    class Meta:
        model = state
        fields = '__all__'
