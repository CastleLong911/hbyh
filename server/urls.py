from django.urls import path
from . import views

urlpatterns = [
    path('get/<moduleName>/<location>/', views.getModule, name='get'),
    path('gps/<moduleName>/<ID>/<location>/', views.gps, name='gps'),
    path('setModule/<moduleName>/<latitude>/<longitude>/', views.setModule, name='set'),
]