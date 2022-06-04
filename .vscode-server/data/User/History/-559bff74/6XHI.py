from pyexpat import model
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from publications.models import Publication
from .api.serializers import PublicationSerializer, SearchSerializer
from rest_framework import filters

# Create your views here.

class PublicationAPIView(APIView):

    def post(self, request):
        serializer = PublicationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "La publicación fue creada con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class PublicationListAPIView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['type_material','volume']


