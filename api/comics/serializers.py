from rest_framework import serializers
from comics.models import Character, Comic


		
class PersonajeSerializer(serializers.Serializer):
	class Meta:
		model = Character
		fields = ('id', 'name', 'image', 'appearances')
	

class ComicSerializer(serializers.Serializer):
	personaje = PersonajeSerializer(read_only=True)
	class Meta:
		model = Comic
		fields = ('user', 'title', 'image', 'onSaleDate')

class CreateComicSerializer(serializers.Serializer):

	class Meta:
		model = Comic
		fields = ('user', 'comic_id', 'title', 'image', 'onSaleDate')





