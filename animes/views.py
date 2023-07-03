from django.shortcuts import render
from rest_framework import generics
from .models import Anime
from .serializers import AnimeSerializer


class AnimesList(generics.ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class AnimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
