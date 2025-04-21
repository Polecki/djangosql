from django.db import models

ANOS = [(ano, ano) for ano in range(1980, 2031)]

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano_lancamento = models.IntegerField(choices=ANOS)
    imagem = models.ImageField(upload_to='filmes/')

    def __str__(self):
        return self.titulo
