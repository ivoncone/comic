from django.shortcuts import render
from django.contrib import messages


from rest_framework import status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView 
from rest_framework.response import Response

from users.models import User
from users.serializers import CreateUserSerializer, UserSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from django.contrib.auth.hashers import check_password



#register new user and see data
class CreateUserView(APIView):
	permission_classes = (AllowAny, )
	def post(self, request):
		serializer = CreateUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'status': 201, 'message': 'este usuario ha sido creado correctamente'})
		else:
			return Response({'status':403, 'message': 'ya existe este usuario'})
#Login view
class LoginView(APIView):
	def post(self, request):
		email = request.data['email']
		password = request.data['password']
		user = User.objects.filter(email=email).first()
		if email is None:
			return Response({'status': 404, 'message': 'No existe el usuario'})
		if not user.check_password(password):
			return Response({'status': 403, 'message':'esta contraseña no es correcta'})

		access = AccessToken.for_user(user)


		return Response({'status': 200,
			'id': user.id,
			'name': user.name,
			'age': user.age,
			'token': str(access),
		})
		
#vista de usuario 
class UserView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request):
		user = User.objects.get(email=request.user)
		if user is not None:
			serializer = UserSerializer(user)
			return Response({'status': 200, 'data': serializer.data})

		


		



