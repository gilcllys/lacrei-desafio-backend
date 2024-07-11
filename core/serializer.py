from rest_framework import serializers
from core import models

class ProfissionalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfissionalProfile
        fields = '__all__'