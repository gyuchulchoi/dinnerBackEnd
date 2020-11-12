from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('kim_menus', views.KimMenuList.as_view()),
    path('kim_menus/<int:pk>', views.KimMenuDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)