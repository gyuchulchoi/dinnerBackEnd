from rest_framework import serializers
from ..models import Bon_Menu

class BonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bon_Menu
        # fields = '__all__'
        # exclude = ['name']
        fields = ['id', 'menu_price', 'menu_name', 'menu_new', 'menu_best', 'menu_type']
