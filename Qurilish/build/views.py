from django.shortcuts import render
from .models import Qurilish_tashkiloti,Qurilish_binosi,Area
from rest_framework import viewsets
from .serializers import AreaSerializer,Qurilish_binosiSerializers,Qurilish_tashkilotiSerializer
# Create your views here.
from  rest_framework.permissions import (IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly)


class AreaApiViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class Qurilish_tashkilotiApiViewSet(viewsets.ModelViewSet):
    queryset = Qurilish_tashkiloti.objects.all()
    serializer_class = Qurilish_tashkilotiSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class Qurilish_binosiApiViewSet(viewsets.ModelViewSet):
    queryset = Qurilish_binosi.objects.all()
    serializer_class = Qurilish_binosiSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]



