from rest_framework import serializers
from ..models import BonMenu

class BonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonMenu
        # fields = '__all__'
        # exclude = ['name']
        fields = ['id', 'menu_price', 'menu_name', 'menu_new', 'menu_best', 'menu_type']
