from .models import Filmes, Generos
from rest_framework import serializers

class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
       model = Generos
       fields = '__all__'  # expõe todos os campos do modelo Generos

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = '__all__'  # expõe todos os campos do modelo Filmes
