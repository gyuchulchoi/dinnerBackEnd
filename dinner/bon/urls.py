from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('bon/', views.BonList.as_view()),
    path('bon/<int:pk>/', views.BonDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)