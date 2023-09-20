from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

import requests
import time
import hashlib

from django_filters import rest_framework as filters

from comics.serializers import ComicSerializer, PersonajeSerializer

from comics.models import Personaje, Comic, Busqueda

from api.settings import MARVEL_BASE_URL, MARVEL_KEY, MARVEL_PRIV_KEY

class MarvelSearchView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        public_key = MARVEL_KEY
        private_key = MARVEL_PRIV_KEY
        timestamp = str(int(time.time()))
        hash_value = hashlib.md5((timestamp + private_key + public_key).encode()).hexdigest()
        params = {
                'apikey': public_key,
                'ts': timestamp,
                'hash': hash_value
        }

        param_charachter = request.query_params.get('characters')
        param_comic = request.query_params.get('comics')
        search_param = request.query_params.get('search', '')

        if param_charachter == 'characters':     
            base_url = MARVEL_BASE_URL+"characters"
            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                data = response.json()["data"]["results"]
                extracted_data = [{'id':character['id'], 'name':character['name'], 'image': character['resourceURI'], 'appearances': character['comics']['available']} for character in data]
                return Response({'data':extracted_data, 'status': 200})
            except requests.exceptions.RequestException as e:
                return Response({'error': 'Unable to fetch data from marvel api', 'status': 500})            
        
        elif param_comic == 'comics':     
            base_url = MARVEL_BASE_URL+"comics"
            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                data = response.json()["data"]["results"]
                extracted_data = [{'id':comic['id'], 'title':comic['title'], 'image':comic['resourceURI'], 'onSaleDate': comic['modified']} for comic in data]
                return Response({'data':extracted_data, 'status': 200})
            except requests.exceptions.RequestException as e:
                return Response({'error': 'Unable to fetch data from marvel api', 'status': 500})
        
        # busqueda de personajes por nombre
        elif search_param is not None:
            # Perform the search based on the query parameter
            queryset = Personaje.objects.filter(name__icontains=search_param)
            base_url = MARVEL_BASE_URL+"characters"
            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                data = response.json()["data"]["results"]
                extracted_data = [{'id':character['id'], 'name':character['name'], 'image':character['resourceURI'], 'appearances':character['comics']['available']} for character in query]
                return Response({'data':extracted_data, 'status': 200})
            except requests.exceptions.RequestException as e:
                return Response({'error': 'Unable to fetch data from marvel api', 'status': 500})

        # todos los personajes de la a-z
        else:
            base_url = MARVEL_BASE_URL+"characters"

            try:
                response = requests.get(base_url, params=params)
                response.raise_for_status()
                data = response.json()["data"]["results"]
                extracted_data = [{'id':character['id'], 'name':character['name'], 'image': character['resourceURI'], 'appearances': character['comics']['available']} for character in data]
                return Response({'data':extracted_data, 'status': 200})
            except requests.exceptions.RequestException as e:
                return Response({'error': 'Unable to fetch data from marvel api', 'status': 500})
            

class CreateComicCollection(APIView):
    permission_classes = (IsAuthenticated)
    def post(self, request):
        serializer = ComicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'message': 'este comic ha sido creado correctamente'})
        else:
            return Response({'status': 500, 'message': 'no existe este comic'})

class RetrieveComicCollection(APIView):
    permission_classes = (IsAuthenticated)
    def get(self, request):
        if User.objects.filter(user=request.user).exists():
            user = User.objects.get(user=request.user)
            comics = Comic.objects.filter(user=user)
            serializer = ComicSerializer(comics, many=True)
            return Response({'status': 200, 'message': 'este comic ha sido creado correctamente'})
        else:
            return Response({'status': 403, 'message': 'No tienes un perfil de usuario con comics guardados'})








