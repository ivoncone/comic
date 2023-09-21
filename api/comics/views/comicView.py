from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from comics.serializers import ComicSerializer

from comics.models import Character, Comic
from users.models import User

class RetrieveComicCollection(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user.id 
        if Comic.objects.filter(user=user).exists():
            comics = Comic.objects.filter(user=user)
            serializer = ComicSerializer(comics, many=True)
            return Response({'status': 200, 'message': 'este comic ha sido creado correctamente'})
        else:
            return Response({'status': 403, 'message': 'No tienes un perfil de usuario con comics guardados'})

