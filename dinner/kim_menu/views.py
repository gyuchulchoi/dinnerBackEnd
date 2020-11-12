from ..models import KimMenu
from .serializers import KimMenuSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class KimMenuList(generics.ListCreateAPIView):
    queryset = KimMenu.objects.all()
    serializer_class = KimMenuSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'name']

class KimMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KimMenu.objects.all()
    serializer_class = KimMenuSerializer
