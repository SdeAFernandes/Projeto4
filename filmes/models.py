from django.db import models

class Generos(models.Model):
   nome = models.CharField(max_length=255)  # GEnero do FIlme

   def __str__(self):
       return self.nome  # representação em string do genero

class Filmes(models.Model):
   titulo = models.CharField(max_length=255)           # título do filme
   generos = models.ForeignKey(Generos, on_delete=models.CASCADE)  # relacionamento com Generos
   descricao = models.CharField(max_length=255)               # código 
   duracao = models.PositiveIntegerField()              # Duração do FIlme(positivo)
   ano_lancamento = models.PositiveIntegerField()                  # ano de publicação (positivo)

   def __str__(self):
       return self.titulo  # representação em string do livro
