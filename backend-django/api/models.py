from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
