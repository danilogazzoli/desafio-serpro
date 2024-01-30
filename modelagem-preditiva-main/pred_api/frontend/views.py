from django.shortcuts import render
from .models import Paciente

# Create your views here.



def paciente_list(request):
    context = {}
    context["paciente_list"] = Paciente.objects.all()
       
    return render(request, 'frontend/paciente_list.html', context=context)


