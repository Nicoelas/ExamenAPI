from django.db import models

class Socio(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    numero_socio = models.IntegerField(unique=True)
    contraseña = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dni
