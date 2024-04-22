import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from geopy.distance import geodesic
from shapely.geometry import Point
import pandas as pd
from .models import Landmark
from django.views.decorators.http import require_POST

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ChatbotInputSerializer


@require_http_methods(["GET"])
def get_location(request):
    try:
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        if latitude is None or longitude is None:
            return JsonResponse({'error': 'Latitude and longitude parameters are required'})

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            return JsonResponse({'error': 'Latitude and longitude must be valid floating point numbers'})

        user_location = Point(longitude, latitude)

        landmarks = Landmark.objects.all()

        distances = []
        for landmark in landmarks:
            landmark_location = Point(landmark.longitude, landmark.latitude)
            distance = geodesic((latitude, longitude), (landmark.latitude, landmark.longitude)).kilometers
            distances.append((landmark, distance))

        sorted_landmarks = sorted(distances, key=lambda x: x[1])

        landmarks_data = []
        for landmark, distance in sorted_landmarks:
            landmarks_data.append({
                'name': landmark.name,
                'latitude': landmark.latitude,
                'longitude': landmark.longitude,
                'description': landmark.description,
                'photo_url': landmark.photo.url,
                'work_schedule': landmark.work_schedule,
                'price': landmark.price,
                'contacts': landmark.contacts,
                'history_fact': landmark.history_fact,
            })

        location_data = {
            'latitude': latitude,
            'longitude': longitude,
            'nearest_landmarks': landmarks_data,
        }
        return JsonResponse(location_data)

    except Exception as e:
        return JsonResponse({'error': str(e)})


