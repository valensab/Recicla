from rest_framework import serializers
from publications.models import Publication
from django.utils import timezone

class PublicationSerializer(serializers.ModelSerializer):

    type_material = serializers.CharField()
    address = serializers.CharField()
    weight = serializers.DecimalField(max_digits=10, decimal_places=3)
    volume = serializers.DecimalField(max_digits=10, decimal_places=3)
    description = serializers.CharField()


    def create(self, validated_data):
        publication = Publication(**validated_data)
        publication.user = validated_data['user']
        publication.type_material = validated_data['type_material']
        publication.weight = validated_data['weight']
        publication.volume = validated_data['volume']
        publication.address = validated_data['address']
        publication.state = True
        publication.timestamp= timezone.now()
        publication.save()
        return publication

    class Meta:
        model = Publication
        fields = "__all__"

class SearchSerializer(serializers.ModelSerializer):
    publication = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = ['publication']