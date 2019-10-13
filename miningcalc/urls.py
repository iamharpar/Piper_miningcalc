from django.urls import path, include
from .views import miningcalc

urlpatterns = [
    path('', miningcalc.as_view(),name='index'),
]