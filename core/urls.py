from rest_framework import routers
from core import viewsets
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'profissionalProfile', viewsets.ProfissionalProfileViewSet)

urlpatterns = [
    path('register/', viewsets.RegisterView.as_view(), name='register')
]

urlpatterns += router.urls