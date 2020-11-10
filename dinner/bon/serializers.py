from rest_framework import serializers
from ..models import Bon

class BonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bon
        # fields = '__all__'
        # exclude = ['name']
        fields = ['id', 'name', 'price', 'type', 'desc']
