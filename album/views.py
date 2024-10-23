from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from album.models import Team, Player
from django.urls import reverse_lazy

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
    
class TeamUpdateView(UpdateView):
    model = Team
    fields = '__all__'

class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    
class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')

class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')