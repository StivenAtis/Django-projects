from django.shortcuts import render
from django.views.generic import ListView, DetailView
from album.models import Team
from album.models import Player

# Create your views here.
class TeamListView(ListView):
    model = Team
    # template_name = 'album/team_list.html'

class PlayerListView(ListView):
    model = Player
    # template_name = 'album/player_list.html'
    
class TeamDetailView(DetailView):
    model = Team

class PlayerDetailView(DetailView):
    model = Player
    