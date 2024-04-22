from rest_framework import serializers
from .models import Landmark


class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmark
        fields = ['id', 'name', 'description', 'latitude', 'longitude', 'photo']


class ChatbotInputSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
