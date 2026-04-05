from rest_framework import serializers
from .models import Filosofo, Exibicao


class FilosofoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filosofo
        fields = ('id', 'nome', 'biografia', 'imagem', 'referencias', 'slug', 'publicado')



class ExibicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exibicao
        fields = ('id_filosofo', 'data_exibicao')