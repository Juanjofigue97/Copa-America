from django.urls import path 
from .views import (
    PlayerUpdate,
    PlayerCreate,
    PlayerDelete,
    PlayerListView,
    PlayerDetailView,
    TeamCreate,
    TeamDetailView,
    TeamUpdate,
    TeamDelete,
    OrderByHeight)

urlpatterns = [
    path('',PlayerListView.as_view(), name='player-list'),
    path('player/create/', PlayerCreate.as_view(), name='player-create'),
    path('player/<int:pk>/detail/', PlayerDetailView.as_view(), name='player-detail'),
    path('player/<int:pk>/update/',PlayerUpdate.as_view(),name='player-update'), 
    path('player/<int:pk>/delete/', PlayerDelete.as_view(), name='player-delete'),
    path('playerByHeight/', OrderByHeight, name='playerByHeight'),

    path('team/create/', TeamCreate.as_view(), name='team-create'),
    path('team/<int:pk>/detail/', TeamDetailView.as_view(), name='team-detail'),
    path('team/<int:pk>/update/',TeamUpdate.as_view(),name='team-update'), 
    path('team/<int:pk>/delete/', TeamDelete.as_view(), name='team-delete'),
]

