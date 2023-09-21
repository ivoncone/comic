from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from comics.serializers import CreateComicSerializer

from comics.models import Character, Comic
from users.models import User

class CreateComicCollection(APIView):
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        serializer = CreateComicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'message': 'este comic ha sido creado correctamente'})
        else:
            return Response({'status': 500, 'message': 'no existe este comic'})

