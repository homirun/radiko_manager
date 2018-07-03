from rest_framework import serializers
from rec_radiko.models import Reserve


class ReserveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserve
        fields = '__all__'
