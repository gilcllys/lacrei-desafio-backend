from rest_framework import generics
from rest_framework import viewsets
from core import serializer, models, validate_serializer, actions
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action


class RegisterView(generics.GenericAPIView):    
    permission_classes = [AllowAny]
    serializer_class = validate_serializer.UsuarioSerializerValidate
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data_serializer = serializer.validated_data
        response = actions.UserAction(data=data_serializer).createUser()
        return response
    
class ProfissionalProfileViewSet(viewsets.ModelViewSet):    
    serializer_class = serializer.ProfissionalProfileSerializer
    queryset = models.ProfissionalProfile.objects.all()
    