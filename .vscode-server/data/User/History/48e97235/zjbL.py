from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from publications.models import Publication
from requests.models import Request
from publications.api.serializers import PublicationSerializer, SearchSerializer



#Publicaciones que han realizado los usuarios
@api_view(['GET'])
def publication_list(request):

    if request.method == 'GET':
        publications = Publication.objects.all()
        publications_serializer = PublicationSerializer(publications,many = True)
        return Response(publications_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Método \"GET\" no permitido.'},status = status.HTTP_400_BAD_REQUEST)

#Publicaciones que han realizado los usuarios - activas
@api_view(['GET'])
def publications_availables_all(request):

    if request.method == 'GET':
        publications = Publication.objects.filter(state=True)
        publications_serializer = PublicationSerializer(publications,many = True)
        return Response(publications_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Método \"GET\" no permitido.'},status = status.HTTP_400_BAD_REQUEST)

#Eliminar publicación
@api_view(['DELETE'])
def publication_delete(request,pk=None):
    # queryset
    print(pk)
    publication = Publication.objects.filter(id_publication = pk).first()

    # validation
    if publication:
        if request.method == 'DELETE':
            publication.state = False
            publication.delete()
            return Response({'message':'La publicación fue eliminada correctamente!'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado ninguna publicación con estos datos'},status = status.HTTP_400_BAD_REQUEST)

#Número de publicaciones respondidas
@api_view(['GET'])
def publication_count(request):

    if request.method == 'GET':
        publications_count = Publication.objects.filter(state = False).count()
        publications_count_true = Publication.objects.filter(state = True).count()
        requests= Request.objects.filter(is_active = True).count()
        requests_waiting = Request.objects.filter(publication__state = True, is_active = True, state = "Pendiente").count()
        requests_collected = Request.objects.filter(state = "Recolectado").count()
        requests_accepted = Request.objects.filter(state = "Aceptada").count()
        requests_rejected = Request.objects.filter(state = "Rechazada").count()
        requests_rejected_available = Request.objects.filter(publication__state = True, state = "Rechazada").count()
        data = {
            "Publicaciones contestadas": publications_count,
            "Publicaciones disponibles": publications_count_true,
            "Solicitudes activas": requests,
            "Solicitudes pendientes": requests_waiting,
            "Solicitudes aceptadas": requests_accepted,
            "Solicitudes rechazadas": requests_rejected,
            "Solicitudes rechazadas pero que aún está disponible el material": requests_rejected_available,
        }
        return Response(data,status = status.HTTP_200_OK)
    
    else:
        return Response({'No hay datos'},status = status.HTTP_400_BAD_REQUEST)

#Publicaciones disponibles por un usuario
@api_view(['GET'])
def publications_availables(request, pk = None):
    if request.method == 'GET':
        publication = Publication.objects.filter(user_id= pk, state = True)
        publication_count = Publication.objects.filter(user_id= pk, state = True).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay publicaciones realizadas'},status = status.HTTP_200_OK)
        else:
            return Response(publication_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Material de reciclaje que fue recolectado
@api_view(['GET'])
def publications_made(request, pk = None):
    if request.method == 'GET':
        publication = Publication.objects.filter(user_id= pk, state = False)
        publication_count = Publication.objects.filter(user_id= pk, state = False).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay material recolectado'},status = status.HTTP_200_OK)
        else:
            data = {
                'Número de publicaciones': publication_count,
                "Publicaciones": publication_serializer.data,
            }
            return Response(publication_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Historial de publicaciones
@api_view(['GET'])
def publications_all(request, pk = None):
    if request.method == 'GET':
        publication = Publication.objects.filter(user_id= pk)
        publication_count = Publication.objects.filter(user_id= pk).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay historial de publicaciones'},status = status.HTTP_200_OK)
        else:
            data = {
                'Número de publicaciones': publication_count,
                "Publicaciones": publication_serializer.data,
            }
            return Response(publication_serializer.data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

#Filtrar publicaciones por material de reciclaje
@api_view(['GET'])
def publication_filter(request, pk = None):      
    if request.method == 'GET':
        publication = Publication.objects.filter(type_material= pk)  
        publication_count = Publication.objects.filter(type_material= pk).count()
        publication_serializer = SearchSerializer(publication,many = True)
        if publication_count == 0:
            return Response({'message': 'No hay publicaciones para este tipo de material'},status = status.HTTP_200_OK)
        else:
            data = {
                'Número de publicaciones': publication_count,
                "Publicaciones": publication_serializer.data,
            }
            return Response(data,status = status.HTTP_200_OK)
    else:
        return Response({'Solo se soporta método GET'},status = status.HTTP_400_BAD_REQUEST)

