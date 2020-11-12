from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('dinner.bon_menu.urls')),
    path('', include('dinner.order.urls'))
]