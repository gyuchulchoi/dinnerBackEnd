from ..models import Order
from .serializers import OrderSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import datetime

class IsOwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # return queryset.filter(orderer="김또임")
        return queryset

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = [DjangoFilterBackend, IsOwnerFilterBackend]
    # filterset_fields = ['name']

    # post -> create -> serializer_class.create()

    def filter_queryset(self, queryset):
        order_datetime = self.request.GET.get('order_datetime')
        aa = datetime.datetime.strptime(order_datetime, "%Y-%m-%d")
        return queryset.filter(create_datetime__lt= aa).date()

    def post(self, request, *args, **kwargs):
        request.data['order_complete'] = 1
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
