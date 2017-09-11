from django.db import models


class GymLog(models.Model):
    created = models.DateTimeField()
    mystic = models.IntegerField()
    valor = models.IntegerField()
    instinct = models.IntegerField()
