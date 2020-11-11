from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'bonmenu', views.BonList)

urlpatterns = [
    path('', include(router.urls)),
    #path('data/', views.BonData),
    #path('bon_menu/<int:pk>/', views.BonDetail.as_view())
]