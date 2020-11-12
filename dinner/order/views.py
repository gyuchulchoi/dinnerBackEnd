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

    def filter_queryset(self, queryset):
        startOfToday = datetime.datetime.today().strftime('%Y-%m-%d')
        endOfToday = datetime.datetime.strptime(startOfToday,'%Y-%m-%d') + datetime.timedelta(days=1, microseconds=-1)
        return queryset.filter(create_datetime__gt = startOfToday, create_datetime__lt = endOfToday)
        # fromDateStr = self.request.query_params.get('fromDate')
        # toDateStr = self.request.query_params.get('toDate')

        # if(fromDateStr is None and toDateStr is None):
        #     a = datetime.datetime.today().strftime('%Y-%m-%d')
        #     b= datetime.datetime.strptime(a,'%Y-%m-%d') + datetime.timedelta(days=1, microseconds=-1)
        #     return queryset.filter(create_datetime__gt = a, create_datetime__lt = b)
        
        # dateFileter = {}
        # if(fromDateStr is not None):
        #     dateFileter['create_datetime__gt'] = datetime.datetime.strptime(fromDateStr, "%Y-%m-%d")
        # if(toDateStr is not None):
        #     dateFileter['create_datetime__lt'] = datetime.datetime.strptime(toDateStr, "%Y-%m-%d")
        
        # return queryset.filter(**dateFileter)    

    def post(self, request, *args, **kwargs):
        request.data['order_complete'] = 1
        return super().post(request, *args, **kwargs)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
