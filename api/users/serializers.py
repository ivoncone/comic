from rest_framework import serializers 

from users.models import User

#serializer for user data view
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'age')

class CreateUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User 
		fields = ('email', 'password', 'name', 'age')

	def create(self, validated_data):
		password = validated_data.pop('password', None)
		instance = self.Meta.model(**validated_data)
		if password is not None:	
			instance.set_password(password)
			instance.save()
			return instance 



