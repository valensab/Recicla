from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from requests.models import Request
from requests.api.serializers import RequestSerializer
from users.models import User
from publications.models import Publication

# Create your views here.

class RequestAPIView(APIView):

    def post(self, request):
        serializer = RequestSerializer(data= request.data)
        if serializer.is_valid():
            user = User.objects.filter(id = request.data['recycler']).first()
            publication = Publication.objects.filter(id_publication = request.data['publication']).first()
            request = Request.objects.filter(recycler = user.id, publication = publication.id_publication, is_active = True).first()
            if (request):
                 return Response({'message':'Ya ha hecho una solicitud para esta publicación'},status = status.HTTP_400_BAD_REQUEST)
            else: 
                if(publication.state == True):
                    serializer.save()
                    return Response({"message": "La solicitud fue enviada con éxito"}, status=status.HTTP_201_CREATED)
            return Response({'message':'La publicación no se encuentra disponible'},status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'Error al enviar la solicitud'},status = status.HTTP_400_BAD_REQUEST)