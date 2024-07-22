from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Turno(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_completada = models.DateTimeField(null = True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '- Usuario: ' + self.user.username
    
