from rest_framework import serializers
from comics.models import Personaje, Comic, Busqueda


#serializer for user data view

class BusquedaSerializer(serializers.Serializer):
	class Meta:
		model = Busqueda
		fields = ('id', 'personaje', 'comic')
		
class PersonajeSerializer(serializers.Serializer):
	class Meta:
		model = Personaje
		fields = ('id', 'name', 'image', 'appearances')
	

class ComicSerializer(serializers.Serializer):
	class Meta:
		model = Comic
		fields = ('id', 'title', 'image', 'onSaleDate')

