from rest_framework import serializers
from comics.models import Character, Comic


#serializer for user data view

		
class PersonajeSerializer(serializers.Serializer):
	class Meta:
		model = Character
		fields = ('id', 'name', 'image', 'appearances')
	

class ComicSerializer(serializers.Serializer):
	personaje = PersonajeSerializer(read_only=True)
	class Meta:
		model = Comic
		fields = ('user', 'title', 'personaje', 'image', 'onSaleDate')

class CreateComicSerializer(serializers.Serializer):
	personaje = PersonajeSerializer(many=True, read_only=True)

	class Meta:
		model = Comic
		fields = ('user', 'title', 'personaje', 'image', 'onSaleDate')

"""
	def create(self, validated_data):
		personaje = validated_data.pop('personaje')
		personaje_obj = Character.objects.create(**validated_data)
		for dato in personaje:
			p = Character.objects.create(name=dato["name"],
					image=dato["image"],
					appearances=dato["appearances"]
				)
			personaje_obj.personaje.add(p)
		return personaje_obj
"""



