from django.urls import path
from . import views

urlpatterns = [
    path('', views.apioverview ,name='apioverview'),
    path('players/', views.display_profile, name='display_profile'),
    path('players/<int:player_id>/', views.display_detail, name='display_detail'),
    path('leagues/', views.display_leagues_profiles, name='display_profile'),
    path('states/', views.display_states_profiles, name='display_profile'),
    path('leagues/<int:league_id>/', views.display_leagues_detail, name='league_details_api'),
    path('players/addplayer/', views.add_new_player, name='add_new_player'),

]