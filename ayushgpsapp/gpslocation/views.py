from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import Coordinate
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def POSTcord(request):
    if request.method == 'GET':
        cords = Coordinate.objects.all()
        return JsonResponse({"Current Coordinates": (cords[0].latitude, cords[0].longitude)})
    if request.method == 'POST':
        Coordinate.objects.all().delete()
        body = request.body
        dict = json.loads(str(request.body).encode('utf-8'))
        newLat = dict['latitude']
        newLong = dict['longitude']
        newCords = Coordinate(longitude = newLong, latitude = newLat)
        newCords.save()
        print newCords.latitude
        print newCords.longitude
        return JsonResponse({"Yes":"Yes"})
@csrf_exempt
def map(request):
    if(Coordinate.objects.all()[0].longitude == "unknown" or Coordinate.objects.all()[0].latitude == "unknown"):
        return HttpResponse("<h1>Error</h1>")

    longitude = Coordinate.objects.all()[0].longitude
    latitude = Coordinate.objects.all()[0].latitude

    # longitude = str(float(rawLongitude)/(-100))
    # latitude = str(float(rawLatitude)/100)

    context= {'lat': latitude, 'long': longitude}
    print(latitude + " " + longitude)
    return render(request, 'gpslocation/index.html',context)
