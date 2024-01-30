from rest_framework import serializers 
from frontend.models import Paciente 
 
class PacienteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Paciente
        fields = ('id',
                  'paciente',
                  'hospital',
                  'idade',
                  'sexo',
                  'TDP',
                  'PAR',
                  'CS',
                  'ASJ',
                  'ECG',
                  'FCM',
                  'AIE',
                  'DST',
                  'IST',
                  'NVP',
                  'talassemia',
                  'diagnostico')