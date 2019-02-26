from django.db import models
from uuid import uuid4
# Create your models here.


class Reserve(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid4, editable=False)
    station_id = models.CharField(max_length=3)
    start_date = models.DateField(auto_now=False)
    start_time = models.TimeField(max_length=255)
    rec_time = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

