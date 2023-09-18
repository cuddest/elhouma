from rest_framework.decorators import api_view
from .serializer import PlayerSerializer,stateSerializer,leagueSerializer
from django.http import JsonResponse
from .models import Player,state,league
from rest_framework.response import Response


def apioverview(request):
	return JsonResponse("API BASE POINT",safe=False)

@api_view(['GET'])
def display_profile(request):
	all_players = Player.objects.all()
	serializer = PlayerSerializer(all_players,many=True)
	return Response(serializer.data)
@api_view(['GET'])
def display_leagues_profiles(request):
	all_leagues = league.objects.all()
	serializer=  leagueSerializer(all_leagues,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def display_states_profiles(request):
	all_states = state.objects.all()
	serializer= stateSerializer(all_states,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def display_detail(request):
	all_players = Player.objects.all()
	serializer = PlayerSerializer(all_players,many=True)
	return Response(serializer.data)

@api_view(['GET'])
def display_leagues_detail(request, league_id):
    league_instance = league.objects.filter(id=league_id)
    serializer = leagueSerializer(league_instance,many=True)
    return Response(serializer.data)

@api_view(['post'])
def add_new_player(request):
    new_player = PlayerSerializer(data=request.data)
    if new_player.is_valid() :
	    new_player.save()
	    return Response(new_player.data)
    return Response(new_player.errors)