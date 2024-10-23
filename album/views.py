from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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
    
class TeamCreateView(CreateView):
    model = Team
    fields = '__all__'

class PlayerCreateView(CreateView):
    model = Player
    fields = '__all__'