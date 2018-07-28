from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.decorators import *
from rest_framework.response import Response
import json
from .get_timetable import *

# Create your views here.
from .models import Reserve
from .serializers import *


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

    @action(methods=['POST'], detail=True)
    def set_reserve(self):
        pass


# TODO: https://stackoverflow.com/questions/45532965/django-rest-framework-serializer-without-a-model <- modelLess views

class TimeTableView(views.APIView):

    @staticmethod
    def get(request):
        timetable = GetTimeTable()
        return Response(timetable.get_timetable())
