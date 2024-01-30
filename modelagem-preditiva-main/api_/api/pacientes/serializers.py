from rest_framework import serializers
from .models import Paciente


class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'


class PacienteListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="pacienteslist-detail")

    class Meta:
        model = Paciente
        fields = '__all__'

