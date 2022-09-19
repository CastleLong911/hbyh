from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Module

def getModule(request, moduleName):
    if Module.objects.filter(moduleName=moduleName):
        return HttpResponse(Module.objects.filter(moduleName=moduleName).values('on'))
    else:
        return HttpResponse("NO MODULE")

def gps(request, moduleName, location, ID):
    if Module.objects.filter(moduleName=moduleName):
        deviceLocation = location.split(',')
        moduleLocation = Module.objects.filter(moduleName=moduleName).values('latitude', 'longitude')
        if abs(moduleLocation[0]['latitude'] - float(deviceLocation[0])) > float(1/3600) or abs(moduleLocation[0]['longitude'] - float(deviceLocation[1])) > float(1/3600):
            Module.objects.filter(moduleName=moduleName).update(on='off')
            return HttpResponse("off")
        else:
            Module.objects.filter(moduleName=moduleName).update(on='on')
            return HttpResponse("on")
    else:
        return HttpResponse("NO MODULE")