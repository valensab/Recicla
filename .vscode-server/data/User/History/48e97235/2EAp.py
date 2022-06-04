from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from publications.models import Publication
from publications.api.serializers import PublicationSerializer

@api_view(['GET'])
def publication_list(request):

    if request.method == 'GET':
        publications = Publication.objects.all()
        publications_serializer = PublicationSerializer(publications,many = True)
        return Response(publications_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Método \"GET\" no permitido.'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def publication_delete(request,pk=None):
    # queryset
    print(pk)
    publication = Publication.objects.filter(id = pk).first()

    # validation
    if publication:
        if request.method == 'DELETE':
            publication.state = False
            publication.save()
            return Response({'message':'La publicación fue eliminada correctamente!'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado ninguna publicación con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def publication_count(request):

    if request.method == 'GET':
        publications_count = Publication.objects.filter(state = True).count()
        data = {
            "count": publications_count
        }
        return Response(data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta metodo GET'},status = status.HTTP_400_BAD_REQUEST)




# @api_view(['POST'])
# def publication_change_password(request,pk=None):
    
#     if request.method == 'POST':
#         Publication = Publication.objects.filter(id = pk).first()
#         if Publication:
#             Publication.set_password(self=Publication ,raw_password=request.data["password"])
#             Publication.save()
#             return Response({"La contraseña se ha cambiado"},status = status.HTTP_200_OK)
#         else:
#             return Response({"El usuario no fue encontrado"},status =  status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response({'Petición inválida'},status = status.HTTP_400_BAD_REQUEST)