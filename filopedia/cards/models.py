from django.db import models
from django.utils import timezone

class Filosofo(models.Model):
    nome = models.CharField(max_length=100, null=False)
    biografia = models.TextField(null=False, blank=False)
    imagem = models.CharField(null=False, blank=False)
    referencias = models.CharField(null=False, blank=False)
    slug = models.CharField(max_length=120, null=False, blank=False)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome}'
class Exibicao(models.Model):
    id_filosofo = models.ForeignKey(Filosofo, on_delete=models.CASCADE)
    data_exibicao = models.DateField(default=timezone.now(), null=False, blank=False)

    def __str__(self):
        return f"{self.id_filosofo.nome}"