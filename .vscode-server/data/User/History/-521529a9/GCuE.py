from rest_framework import serializers
from users.models import User
from django.utils import timezone
from rest_framework.authtoken.models import Token

class UserTokenSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email','password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user

class UserFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','last_name','email','is_provider','is_recycler']

class ProviderSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    phone_number = serializers.CharField()
    address = serializers.CharField()


    def create(self, validated_data):
        provider = User(**validated_data)
        provider.name = validated_data['name']
        provider.last_name = validated_data['last_name']
        provider.email = validated_data['email']
        provider.phone_number = validated_data['phone_number']
        provider.address = validated_data['address']
        provider.is_provider = True
        provider.last_login = timezone.now()
        provider.set_password(validated_data['password'])
        provider.save()
        return provider


    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Ya existe un usuario con este correo electrónico")
        return lower_email

    def update(self,instance,validated_data):
        updated_provider = super().update(instance,validated_data)
        update_provider.name = validated_data['name']
        update_provider.last_name = validated_data['last_name']
        update_provider.email = validated_data['email']
        update_provider.phone_number = validated_data['phone_number']
        update_provider.address = validated_data['address']
        update_provider.is_provider = True
        update_provider.last_login = timezone.now()
        update_provider.set_password(validated_data['password'])
        update_provider.save()
        return updated_provider

    class Meta:
        model = User
        fields = "__all__"


class RecyclerSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    phone_number = serializers.CharField()

    def create(self, validated_data):
        recycler = User(**validated_data)
        recycler.email = validated_data['email']
        recycler.name = validated_data['name']
        recycler.last_name = validated_data['last_name']
        recycler.phone_number = validated_data['phone_number']
        recycler.is_recycler = True
        recycler.last_login = timezone.now()
        recycler.set_password(validated_data['password'])
        recycler.save()
        return recycler

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Ya existe un usuario con este correo electrónico")
        return lower_email

    def update(self,instance,validated_data):
        update_recycler = super().update(instance,validated_data)
        update_recycler.email = validated_data['email']
        update_recycler.name = validated_data['name']
        update_recycler.last_name = validated_data['last_name']
        update_recycler.phone_number = validated_data['phone_number']
        update_recycler.is_recycler = True
        update_recycler.last_login = timezone.now()
        update_recycler.set_password(validated_data['password'])
        update_recycler.save()
        return update_recycler

    class Meta:
        model = User
        fields = "__all__"


class NameRecyclerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','last_name']
    