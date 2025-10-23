from rest_framework.routers import DefaultRouter
from django.urls import path, include
from equipos.views import (EquipoViewSet)

router = DefaultRouter()
router.register(r'equipo', EquipoViewSet, basename='equipo')

urlpatterns = [
    path('', include(router.urls)),
]
