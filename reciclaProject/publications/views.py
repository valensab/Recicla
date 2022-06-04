from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from publications.models import Publication, User
from publications.api.serializers import PublicationSerializer
# Create your views here.

class PublicationAPIView(APIView):

    def post(self, request):
        serializer = PublicationSerializer(data= request.data)
        user = User.objects.filter(id = request.data['user'], is_provider = True).first()
        if serializer.is_valid():
            if user:
                serializer.save()
                return Response({"message": "La publicación fue creada con éxito"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "El usuario no es proveedor"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicationUpdateAPIView(APIView):      
    def put(self, request, pk, format=None):
        publication = Publication.objects.filter(id_publication = pk).first()
        serializer = PublicationSerializer(publication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "La publicación fue modificada con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)