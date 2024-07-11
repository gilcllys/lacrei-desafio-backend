from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class UserAction():
    def __init__(self, data) -> None:
        self.data = data
    
    def createUser(self):
        user = User.objects.create_superuser(
            username=self.data.get('username'),
            email=self.data.get('email'),
            password=self.data.get('password')
        )
        if user:
            return Response(
                    'Perfil criado com sucesso',
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                'Error de cadastro',
                status=status.HTTP_400_BAD_REQUEST
            )