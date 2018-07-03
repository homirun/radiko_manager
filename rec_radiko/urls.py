from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register('reserve', views.ReserveViewSet)

urlpatterns = [
    url('^', include(router.urls)),
]