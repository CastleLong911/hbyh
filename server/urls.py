from django.urls import path
from . import views

urlpatterns = [
    path('get/<moduleName>/', views.getModule, name='get'),
    path('gps/<moduleName>/<ID>/<location>/', views.gps, name='gps'),
]
