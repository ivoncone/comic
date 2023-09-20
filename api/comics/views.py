from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, viewsets
from rest_framework.response import Response
import requests
import time
import hashlib

from django_filters import rest_framework as filters

from comics.serializers import ComicSerializer, PersonajeSerializer, BusquedaSerializer

from comics.models import Personaje, Comic, Busqueda

from api.settings import MARVEL_BASE_URL, MARVEL_KEY, MARVEL_PRIV_KEY

class MarvelSearchView(APIView):
    def get(self, request):
        public_key = MARVEL_KEY
        private_key = MARVEL_PRIV_KEY
        
        timestamp = str(int(time.time()))
        hash_value = hashlib.md5((timestamp + private_key + public_key).encode()).hexdigest()
        base_url = MARVEL_BASE_URL +"characters"
        params = {
            'apikey': public_key,
            'ts': timestamp,
            'hash': hash_value
        }

        try:
            response = requests.get(base_url, params=params)
            print(response)
            response.raise_for_status()
            data = response.json()["data"]["results"]
            print(data)
            
            serializer = BusquedaSerializer(data, many=True)
            return Response({'data':serializer.data, 'status': 200})
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Unable to fetch data from marvel api', 'status': 500})










