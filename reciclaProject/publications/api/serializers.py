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
        
    def update(self, instance, validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.user = validated_data['user']
        updated_user.type_material = validated_data['type_material']
        updated_user.weight = validated_data['weight']
        updated_user.volume = validated_data['volume']
        updated_user.address = validated_data['address']
        updated_user.state = True
        updated_user.timestamp= timezone.now()
        updated_user.save()
        return updated_user
    class Meta:
        model = Publication
        fields = "__all__"
        ordening = ['timestamp']

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"
        ordening = ['timestamp']