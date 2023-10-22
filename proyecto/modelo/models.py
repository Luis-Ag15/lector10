from django.db import models

# Create your models here.

# Modelo que representa la tabla Alumnos
class Alumno(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=30, null=True)
    telefono = models.CharField(max_length=20, null=True)
    status = models.CharField(max_length=20, null=True)
    foto_perfil = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.nombre} - {self.email}  - {self.telefono} '

    class Meta:
        db_table = 'alumnos'
        ordering = ['-created_at']
