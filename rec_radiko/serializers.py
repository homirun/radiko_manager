from rest_framework import serializers
from rec_radiko.models import Reserve


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = ('station_id', 'start_date', 'start_time', 'title', 'rec_time')
        read_only_fields = ('uuid',)
