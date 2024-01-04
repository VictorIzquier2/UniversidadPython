from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona

# Create your views here.

def bienvenido(request):
  no_personas_var = Persona.objects.count()
  personas_var = Persona.objects.all()
  return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas_var})