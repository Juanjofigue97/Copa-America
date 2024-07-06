from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Team, Player

# Create your views here.
class TeamListView(ListView):
    model = Team

class TeamDetailView(DetailView):
    model = Team

class PlayerListView(ListView):
    model = Player

class PlayerDetailView(DetailView):
    model = Player