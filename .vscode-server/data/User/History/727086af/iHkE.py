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
            print(request)
            if (request):
                 return Response({'message':'Ya ha hecho una solicitud para esta publicación'},status = status.HTTP_400_BAD_REQUEST)
            else: 
                if(publication.state == True):
                    serializer.save()
                    return Response({"message": "La solicitud fue enviada con éxito"}, status=status.HTTP_201_CREATED)
            return Response({'message':'La publicación no se encuentra disponible'},status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'Error al enviar la solicitud'},status = status.HTTP_400_BAD_REQUEST)

class RequestAcceptAPIView(APIView):

    def post(self, request):
        serializer = RequestAcceptSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data['publication'])
            request_recycler = Request.objects.filter(id_request=request.data['id_request'], is_active=True).first()
            if request_recycler:
                if serializer.data['recycler'] == request_recycler.recycler.id:
                    publication=Publication.objects.filter(id_publication=request_recycler.publication.id_publication).first()
                    if serializer.data['publication']== publication.id_publication:     
                        publication.state=False
                        request_recycler.is_active=False
                        request_recycler.state="Aceptada"
                        request_recycler.comments="La solicitud fue aceptada"
                        request_recycler.save()
                        publication.save()

                        for request_other in Request.objects.filter(publication=request_recycler.publication.id_publication, is_active=True):
                            request_other.is_active=False
                            request_other.state="Rechazada"
                            request_other.comments="La solicitud ha sido rechazada"
                            request_other.save()
                            return Response({"message": "La solicitud fue aceptada"}, status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "La solicitud no corresponde con esta publicación"},  status=status.HTTP_400_BAD_REQUEST)
                else: 
                    return Response({"message": "La solicitud no corresponde con este reciclador"},  status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "La solicitud ya fue contestada"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

