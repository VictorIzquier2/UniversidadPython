from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona, Domicilio

# Create your views here.

def bienvenido(request):
  no_personas_var = Persona.objects.count()
  no_domicilios_var = Domicilio.objects.count()
  personas_var = Persona.objects.all().order_by('id')
  domicilios_var = Domicilio.objects.all().order_by('id')
  return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas_var, 'no_domicilios': no_domicilios_var, 'domicilios': domicilios_var})