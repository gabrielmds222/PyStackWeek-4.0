from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    return HttpResponse("Você está na página de cadastro")
