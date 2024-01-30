from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from frontend.models import Paciente 
from pred.serializers import PacienteSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def pacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        
        paciente = request.query_params.get('paciente', None)
        if paciente is not None:
            pacientes = pacientes.filter(paciente__icontains=paciente)
        
        pacientes_serializer = PacienteSerializer(pacientes, many=True)
        return JsonResponse(pacientes_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    '''
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    '''     