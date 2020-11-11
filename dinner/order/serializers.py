from rest_framework import serializers
from ..models import Order
import datetime

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        validated_data['create_datetime'] = datetime.datetime.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)