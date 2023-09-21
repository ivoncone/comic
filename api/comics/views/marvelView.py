from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import requests
from ..hashers import payload

from api.settings import MARVEL_BASE_URL
#vista para filtros de comics y personajes
class MarvelSearchView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        params = payload()
        character = request.query_params.get('character')
        comic = request.query_params.get('comic')
        search = request.query_params.get('search')
        
        try:
                # busqueda de personajes CA3
                if character is not None:
                    base_url = f"{MARVEL_BASE_URL}characters?name={character}"
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    data = response.json()["data"]["results"]     
                    extracted_data = [{'id':character['id'], 'name':character['name'], 
                            'image': character['resourceURI'], 
                            'appearances': character['comics']['available']} for character in data]
                    filtered_data = [item for item in extracted_data 
                            if character.lower() in item['name'].lower()]
                    return Response({'data':filtered_data, 'status': 200})           
        
                # busqueda de comics CA3
                elif comic is not None:     
                    base_url = f"{MARVEL_BASE_URL}comics?title={comic}"
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    data = response.json()["data"]["results"]  
                    extracted_data = [{'id':comic['id'], 'title':comic['title'], 
                            'image':comic['resourceURI'], 
                            'onSaleDate': comic['modified']} for comic in data]
                    filtered_data = [item for item in extracted_data 
                            if comic.lower() in item['title'].lower()]
                    return Response({'data':filtered_data, 'status': 200})
    
                # busqueda de personajes y comics por nombre  CA1
                elif search is not None:
                # Perform the search based on the query parameter
                    base_url = f"{MARVEL_BASE_URL}characters?nameStartsWith={search}"
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    data = response.json()["data"]["results"]  
                    extracted_data = [{'id':character['id'], 'name':character['name'], 
                        'image':character['resourceURI'], 'appearances':character['comics']['items']} for character in data]
                    search_result = [item for item in extracted_data if search.lower() in item['name'].lower()]
                    return Response({'data':search_result, 'status': 200})

                # todos los personajes de la a-z CA2
                else:
                    base_url = f"{MARVEL_BASE_URL}characters"
                    response = requests.get(base_url, params=params)
                    response.raise_for_status()
                    data = response.json()["data"]["results"]
                    extracted_data = [{'id':character['id'], 
                        'name':character['name'], 
                        'image':character['resourceURI'], 
                        'appearances':character['comics']['items']} for character in data]
                    return Response({'data':extracted_data, 'status': 200})
        except requests.exceptions.RequestException as e:
            return Response({'error': 'Unable to fetch data from marvel api', 'status': 500})
            








