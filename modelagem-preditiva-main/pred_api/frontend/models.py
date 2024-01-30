from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Paciente(models.Model):
    paciente = models.IntegerField()
    hospital = models.CharField(max_length=1)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1) 
    TDP = models.IntegerField(blank=True, null=True)
    PAR = models.FloatField(blank=True, null=True)
    CS = models.FloatField(blank=True, null=True)
    ASJ = models.IntegerField(blank=True, null=True)
    ECG = models.IntegerField(blank=True, null=True)
    FCM = models.FloatField(blank=True, null=True)
    AIE = models.IntegerField(blank=True, null=True)
    DST = models.FloatField(blank=True, null=True)
    IST = models.IntegerField(blank=True, null=True)
    NVP = models.IntegerField(blank=True, null=True)
    talassemia = models.IntegerField(blank=True, null=True)
    diagnostico = models.IntegerField(blank=True, null=True)

    

    def __str__():
        return self.paciente



