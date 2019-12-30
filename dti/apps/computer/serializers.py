from .models import TiComputer
from rest_framework import serializers


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiComputer
        fields = ['url', 'cp_name']
