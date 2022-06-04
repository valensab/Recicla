from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from users.api.serializers import UserSerializer

@api_view(['GET'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.filter(is_active = True)
        users_serializer = UserSerializer(users,many = True)
        return Response(users_serializer.data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Método \"GET\" no permitido.'},status = status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def user_delete(request,pk=None):
    # queryset
    print(pk)
    user = User.objects.filter(id = pk).first()

    # validation
    if user:
        if request.method == 'DELETE':
            user.is_active = False
            user.save()
            return Response({'message':'Usuario eliminado correctamente!'},status = status.HTTP_200_OK)

    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_count(request):

    if request.method == 'GET':
        users_count = User.objects.filter(is_active = True).count()
        data = {
            "count": users_count
        }
        return Response(data,status = status.HTTP_200_OK)
    
    else:
        return Response({'Solo se soporta metodo GET'},status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_change_password(request,pk=None):
    
    if request.method == 'POST':
        user = User.objects.filter(id = pk).first()
        if user:
	        
            User.set_password(self=user ,raw_password=request.data["password"])
            user.save()
            return Response({"La contraseña se ha cambiado"},status = status.HTTP_200_OK)
	    else:
            return Response({"El usuario no fue encontrado"},status =  status.HTTP_400_BAD_REQUEST)
    else:
         return Response({'Petición inválida'},status = status.HTTP_400_BAD_REQUEST)
