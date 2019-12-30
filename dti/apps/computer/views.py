from .models import TiComputer
from rest_framework import viewsets
from .serializers import ComputerSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = TiComputer.objects.all()
    serializer_class = ComputerSerializer
