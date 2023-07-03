from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ('id', 'added_by', 'name', 'desc', 'created_at', 'updated_at')
