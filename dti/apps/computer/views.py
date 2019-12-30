from rest_framework import viewsets

from .serializers import *


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = TiComputer.objects.all()
    serializer_class = ComputerSerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = TiMonitor.objects.all()
    serializer_class = MonitorSerializer


class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = TiKeyboard.objects.all()
    serializer_class = KeyboardSerializer


class MouseViewSet(viewsets.ModelViewSet):
    queryset = TiMouse.objects.all()
    serializer_class = MouseSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = TiOffice.objects.all()
    serializer_class = OfficeSerializer


class OperatingSystemViewSet(viewsets.ModelViewSet):
    queryset = TiOperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = TiPosition.objects.all()
    serializer_class = PositionSerializer


class ResponsibleViewSet(viewsets.ModelViewSet):
    queryset = TiResponsible.objects.all()
    serializer_class = ResponsibleSerializer


class TowerViewSet(viewsets.ModelViewSet):
    queryset = TiTower.objects.all()
    serializer_class = TowerSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = TiBrand.objects.all()
    serializer_class = BrandSerializer
