from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.decorators import *
from rest_framework.response import Response
from .get_timetable import *
from .models import Reserve
from .serializers import *
from glob import glob
import os


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer

    @action(methods=['GET'], detail=True)
    def set_reserve(self):
        print("post")


class TimeTableView(views.APIView):
    @staticmethod
    def get(request):
        timetable = GetTimeTable()
        return Response(timetable.get_timetable())


class RadioDirView(views.APIView):
    @staticmethod
    def get(request):
        files = glob('./out/*.mp3')
        out = []
        for f in files:
            out.append(os.path.basename(f))
        return Response(out)

