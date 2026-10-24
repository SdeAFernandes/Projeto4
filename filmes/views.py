from .models import Filmes, Generos
from .serializers import FilmesSerializer, GenerosSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'genero__nome', 'ano']