from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register('reserve', views.ReserveViewSet)
#router.register('timetables', views.TimeTableView, base_name="time-tables")

urlpatterns = [
    url('^', include(router.urls)),
    url('timetables', views.TimeTableView.as_view(), name="timetables")
]