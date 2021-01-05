from django.db import models

# Create your models here.
class Participante ():
    nome = models.CharField(max_length=70)
    telefone = models.CharField(max_length=11)
    observacao = models.TextField (null=True, blank=True)
    observacao2 = models.TextField(null=True, blank=True)


