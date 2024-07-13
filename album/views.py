from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Team, Player

# Create your views here.
class TeamListView(ListView):
    model = Team

class TeamDetailView(DetailView):
    model = Team

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__' 

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')

class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    model = Player

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__' 

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')