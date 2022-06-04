from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from requests.models import Request
from requests.api.serializers import RequestSerializer, SearchSerializer
from users.models import User
from publications.models import Publication

@api_view(['GET'])
def request_list(request):

    if request.method == 'GET':
        requests = Request.objects.all()
        requests_serializer = RequestSerializer(requests,many = True)
        return Response(requests_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Método \"GET\" no permitido.'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def requests_availables(request, pk = None):

    if request.method == 'GET': 
        publication = Publication.objects.filter(user_id = pk, state = True)
        for iterar in publication:
            print(iterar)
            publication_consult += Request.objects.filter(publication_id = iterar.id_publication, is_active = True)
            print(publication_consult)
            request_serializer = SearchSerializer(publication_consult, many = True)
        return Response(request_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST','OPTIONS'])
def accepted_request(request,pk=None):
    request_recycler = Request.objects.filter(id_request = pk, is_active = True).first()
    if request_recycler:
        if request.method == 'POST':
            publication = Publication.objects.filter(id_publication = request_recycler.publication.id_publication).first()
            publication.state = False
            request_recycler.is_active = False
            request_recycler.state = "Aceptada"
            request_recycler.comments = "La solicitud fue aceptada"
            request_recycler.save()
            publication.save()

            for request_other in Request.objects.filter(publication = request_recycler.publication.id_publication, is_active=True):
                request_other.is_active = False
                request_other.state = "Rechazada"
                request_other.comments = "La solicitud ha sido rechazada"
                request_other.save()
            
            return Response({"message": "La solicitud fue aceptada"},status = status.HTTP_200_OK)
        else:
            return Response({'message':'Error al cambiar el estado de la solicitud'},status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'La solicitud ya fue contestada'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST','OPTIONS'])
def reject_request(request,pk=None):
    request_recycler = Request.objects.filter(id_request = pk, is_active = True).first()
    if request_recycler:
        if request.method == 'POST':
            request_recycler.is_active = False
            request_recycler.state = "Rechazada"
            request_recycler.comments = "La solicitud ha sido rechazada"
            request_recycler.save()
            
            return Response({"message": "La solicitud fue rechazada"},status = status.HTTP_200_OK)
        else:
            return Response({'message':'Error al cambiar el estado de la solicitud'},status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':'La solicitud ya fue contestada'},status = status.HTTP_400_BAD_REQUEST)

