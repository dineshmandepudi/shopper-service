
from django.db import models


class StoreData(models.Model):
    file_content = models.FileField()
    file_name = models.CharField(max_length=300)

    objects = models.Manager()
