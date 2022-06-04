from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from requests.models import Request
from requests.api.serializers import RequestSerializer, SearchSerializer
from users.models import User
from publications.models import Publication

#Lista de solicitudes realizadas por los usuarios
@api_view(['GET'])
def request_list(request):

    if request.method == 'GET':
        requests = Request.objects.all()
        requests_serializer = RequestSerializer(requests,many = True)
        return Response(requests_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'No hay solicitudes'},status = status.HTTP_400_BAD_REQUEST)

#Solicitudes disponibles para una publicación 
@api_view(['GET'])
def requests_availables(request, pk = None):

    if request.method == 'GET': 
        publication_consult = Request.objects.filter(publication__user_id = pk, publication__state = True, is_active = True)
        publication_count = Request.objects.filter(publication__user_id = pk, publication__state = True, is_active = True).count()
        request_serializer = SearchSerializer(publication_consult, many = True)
        if publication_count == 0:
            return Response({'message': 'No hay solicitudes para esta publicación'},status = status.HTTP_200_OK)
        else: 
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Solicitudes vigentes por un reciclador
@api_view(['GET'])
def requests_availables_recycler(request, pk = None):

    if request.method == 'GET': 
        recycler_consult = Request.objects.filter(recycler = pk, publication__state = True, is_active = True)
        recycler_count = Request.objects.filter(recycler = pk, publication__state = True, is_active = True).count()
        request_serializer = SearchSerializer(recycler_consult, many = True)
        if recycler_count == 0:
            return Response({'message': 'No ha hecho solicitudes'},status = status.HTTP_200_OK)
        else: 
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Solicitudes contestadas a un reciclador
@api_view(['GET'])
def requests_made_recycler(request, pk = None):

    if request.method == 'GET': 
        recycler_consult = Request.objects.filter(recycler = pk, publication__state = False, is_active = False)
        recycler_count = Request.objects.filter(recycler = pk, publication__state = False, is_active = False).count()
        request_serializer = SearchSerializer(recycler_consult, many = True)
        if recycler_count == 0:
            return Response({'message': 'No hay solicitudes contestadas'},status = status.HTTP_200_OK)
        else: 
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Historial de solicitudes
@api_view(['GET'])
def requests_all_recycler(request, pk = None):

    if request.method == 'GET': 
        recycler_consult = Request.objects.filter(recycler = pk)
        recycler_count = Request.objects.filter(recycler = pk).count()
        request_serializer = SearchSerializer(recycler_consult, many = True)
        if recycler_count == 0:
            return Response({'message': 'No hay historial de solicitudes'},status = status.HTTP_200_OK)
        else: 
            return Response(request_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Solicitud aceptada
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

#Solicitud rechazada
@api_view(['POST','OPTIONS'])
def reject_request(request,pk=None):
    request_recycler = Request.objects.filter(id_request = pk, is_active = True, state = "Pendiente").first()
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

@api_view(['POST','OPTIONS'])
def reject_collected(request,pk=None):
    request_recycler = Request.objects.filter(id_request = pk, is_active = True, state = "Aceptada").first()
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
