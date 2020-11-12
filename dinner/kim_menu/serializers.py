from rest_framework import serializers
from ..models import KimMenu
import datetime

class KimMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = KimMenu
        fields = '__all__'