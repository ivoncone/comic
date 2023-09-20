from rest_framework import serializers
from comics.models import Personaje, Comic


#serializer for user data view

		
class PersonajeSerializer(serializers.Serializer):
	class Meta:
		model = Personaje
		fields = ('id', 'name', 'image', 'appearances')
	

class ComicSerializer(serializers.Serializer):
	personaje = PersonajeSerializer(read_only=True)
	class Meta:
		model = Comic
		fields = ('id', 'title', 'personaje', 'image', 'onSaleDate')

