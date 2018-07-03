from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import *
# Create your views here.
from .models import Reserve
from .serializers import ReserveSerializer


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

    @detail_route(methods=['POST'])
    def set_reserve(self):
        pass
