from rest_framework import serializers

from .models import *


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiComputer
        fields = '__all__'


class MonitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiMonitor
        fields = '__all__'


class KeyboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiKeyboard
        fields = '__all__'


class MouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiMouse
        fields = '__all__'


class OfficeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiOffice
        fields = '__all__'


class OperatingSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiOperatingSystem
        fields = '__all__'


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiPosition
        fields = '__all__'


class ResponsibleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiResponsible
        fields = '__all__'


class TowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TiTower
        fields = '__all__'
