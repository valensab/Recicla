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
        fields = ['publication', 'recycler', 'state','id_request']

    def to_representation(self, instance):
        return{
            'id_publication': instance.publication.id_publication,
            'type_material': instance.publication.type_material,
            'address': instance.publication.address,
            'weight':instance.publication.weight, 
            'volume': instance.publication.volume,
            'description': instance.publication.description,
            'timestamp': instance.publication.timestamp,
            'state': instance.publication.state,
            'user': instance.publication.user_id,
            'recycler': instance.recycler.name + " " + instance.recycler.last_name,
            'id_request': instance.id_request,
            'state_request': instance.state
        }
class SearchSerializer(serializers.ModelSerializer):
    #publication  = serializers.StringRelatedField()
    recycler = serializers.StringRelatedField()
    class Meta:
        model = Publication
        fields = ['publication', 'recycler', 'state','id_request']