from rest_framework import serializers
from album.models import Player

class PLayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class PLayerSerializerByheight(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name','last_name','height']

class PLayerUpdateAPI(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name','last_name','height','weight','comment']
        