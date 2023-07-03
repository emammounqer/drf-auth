from django.urls import path
from .views import AnimesList, AnimeDetail

urlpatterns = [
    path('', AnimesList.as_view(), name='animes_list'),
    path('<int:pk>/', AnimeDetail.as_view(), name='thing_detail'),
]
