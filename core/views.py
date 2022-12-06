from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Cidade
import json

# Create your views here.

def cidades(request, estado):
    data = serialize("json", Cidade.objects.filter(estado=estado), fields=('nome', 'capital'))
    return HttpResponse(data)

    