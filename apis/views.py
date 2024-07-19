from rest_framework import generics
from album.models import Player
from .serializers import PLayerSerializer, PLayerSerializerByheight, PLayerUpdateAPI
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class PlayerAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PLayerSerializer

class PlayerByHeightAPIView(generics.ListAPIView):
    queryset = Player.objects.all().order_by('height')
    serializer_class = PLayerSerializerByheight

class PlayerAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PLayerUpdateAPI


    
