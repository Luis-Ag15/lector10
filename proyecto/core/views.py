from django.shortcuts import render
import json

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from modelo import models

# Create your views here.

def inicio(request):
    return render (request, "core/index.html")

def view_detalles_alumno(request):
    if request.method == 'POST':
        result_qr = request.POST.get('datoqr')
        try:
            alumnoBD = models.Alumno.objects.get(id=result_qr)
            # Retorna el ID si existe
            return JsonResponse({'id_alumno': alumnoBD.id})
        except models.Alumno.DoesNotExist:
            return JsonResponse({'id_alumno': 0})  # Retorna 0 si no existe
    return JsonResponse({'error': 'Solicitud no válida'})


def detalles_alumno(request):  # Agrega 'id' como parámetro en la definición de la vista
    id_alumno = request.GET.get('id')
    if id_alumno is not None:
        try:
            alumno = models.Alumno.objects.get(id=id_alumno)
            return render(request, "core/detalles_alumno.html", {"alumno": alumno})
        except models.Alumno.DoesNotExist:
            error_message = f"No existe ningún registro para el ID de alumno: {id}"
            return render(request, "error.html", {"error_message": error_message})
    else:
        return JsonResponse("No se proporcionó el parámetro 'id' en la URL.")
