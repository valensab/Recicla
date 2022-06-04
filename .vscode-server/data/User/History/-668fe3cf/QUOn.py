from rest_framework import serializers
from requests.models import Request
from rest_framework import serializers
from publications.api.serializers import PublicationSerializer
from users.api.serializers import NameRecyclerSerializer

class RequestSerializer(serializers.ModelSerializer):
        
    def create(self, validated_data):
        request = Request(**validated_data)
        request.recycler = validated_data['recycler']
        request.publicacion = validated_data['publication']
        request.comments = "Se envió la solicitud"
        request.is_active = True
        request.save()
        return request
    class Meta:
        model = Request
        fields = '__all__'

class SearchSerializer(serializers.ModelSerializer):
    #publication  = serializers.StringRelatedField()
    recycler = serializers.StringRelatedField()
    class Meta:
        model = Request
        fields = ['publication', 'recycler', 'state']

    def to_representation(self, instance):
        return{
            'publication': instance.publicacion.id_publication,
 
        }