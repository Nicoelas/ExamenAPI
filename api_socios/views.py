from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Socio
import json

@method_decorator(csrf_exempt, name='dispatch')
class SocioList(APIView):
    def get(self, request):
        socios = Socio.objects.all().values('dni', 'numero_socio', 'contraseña')
        return JsonResponse(list(socios), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        socio = Socio.objects.create(dni=data['dni'], numero_socio=data['numero_socio'], contraseña=data['contraseña'])
        return JsonResponse({'id': socio.id, 'dni': socio.dni, 'numero_socio': socio.numero_socio}, status=status.HTTP_201_CREATED)

@method_decorator(csrf_exempt, name='dispatch')
class SocioDetalle(APIView):
    def post(self, request, pk):
        data = json.loads(request.body)
        socio = Socio.objects.get(id=pk)
        socio.contraseña = data.get('contraseña', socio.contraseña)
        socio.save()
        return JsonResponse({'mensaje': 'Contraseña actualizada con éxito'}, status=status.HTTP_200_OK)