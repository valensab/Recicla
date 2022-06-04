from rest_framework import serializers
from requests.models import Request
from rest_framework import serializers
from publications.api.serializers import PublicationSerializer

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
    publication  = PublicationSerializer()
    class Meta:
        model = Request
        fields = '__all__'
