from django.db import models
# from data_retriever import get_all_data
# from constants import DATA_PATH
# import json


# Create your models here.
class Filosofo(models.Model):
    nome = models.CharField(max_length=100, null=False)
    biografia = models.TextField(null=False, blank=False)
    imagem = models.CharField(null=False, blank=False)
    referencias = models.CharField(null=False, blank=False)
    slug = models.CharField(max_length=120, null=False, blank=False)
    publicado = models.BooleanField(default=True)