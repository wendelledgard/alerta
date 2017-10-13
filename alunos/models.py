from django.db import models

class Aluno(models.Model):
    Matricula = models.CharField(max_length=20)
    Ano_letivo = models.IntegerField()
    Faltas = models.FloatField()
    Media_Final = models.FloatField()
    Frequencia = models.FloatField()
    Sexo = models.CharField(max_length=1)
    Renda = models.FloatField()
    Tipo_Escola_Origem = models.CharField(max_length=100)
    Etnia = models.CharField(max_length=20)
    Reside = models.CharField(max_length=100)
    CoefRendimento = models.FloatField()
    AcessoBiblioteca = models.FloatField()
    ETEP = models.FloatField()
    Projeto = models.FloatField()
    BolsaEstudo = models.FloatField()
    Situacao = models.CharField(max_length=20)
    filtro = models.IntegerField()

    def __str__(self):
        return self.Matricula