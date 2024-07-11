from rest_framework import serializers


class UsuarioSerializerValidate(serializers.Serializer):
    email = serializers.EmailField(
        required=True, 
        allow_null=False
    )
    username = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=124,   
    )
    password = serializers.CharField(
        required=True, 
        allow_null=False, 
    )

class ProfissionalProfileSerializerValidate(serializers.Serializer):
    user = serializers.IntegerField(
        required=True, 
        allow_null=False,
    )
    
    completeName = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=128,  
    )
    socialName = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=48,  
    )
    address = serializers.CharField(
        required=True, 
        allow_null=False,
        max_length=128,
    )
    telephone = serializers.IntegerField(
        required=True, 
        allow_null=False,
    )
    email = serializers.EmailField(
        required=True, 
        allow_null=False
    )