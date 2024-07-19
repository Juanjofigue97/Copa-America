from django.urls import path
from .views import PlayerAPIView,PlayerByHeightAPIView,PlayerAPIDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'players', PlayerAPIView)

urlpatterns = [
    path("", PlayerAPIView.as_view(), name="api-player-list"),
    path("playerByHeigth/", PlayerByHeightAPIView.as_view(), name="api-player-list-height"),
    path("<int:pk>/detail", PlayerAPIDetail.as_view(), name="api-player-detail"),
    
]
