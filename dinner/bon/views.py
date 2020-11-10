from ..models import Bon
from .serializers import BonSerializer
from rest_framework import generics


class BonList(generics.ListCreateAPIView):
    queryset = Bon.objects.all()
    serializer_class = BonSerializer

class BonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bon.objects.all()
    serializer_class = BonSerializer
