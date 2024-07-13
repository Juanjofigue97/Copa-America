from django.urls import path 
from .views import PlayerUpdate,PlayerCreate,PlayerDelete,PlayerListView,PlayerDetailView

urlpatterns = [
    path('',PlayerListView.as_view(), name='player-list'),
    path('player/create/', PlayerCreate.as_view(), name='player-create'),
    path('player/<int:pk>/detail/', PlayerDetailView.as_view(), name='player-detail'),
    path('player/<int:pk>/update/',PlayerUpdate.as_view(),name='player-update'), 
    path('player/<int:pk>/delete/', PlayerDelete.as_view(), name='player-delete'),
]

