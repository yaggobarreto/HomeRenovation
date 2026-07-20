from django.db import models

# Create your models here.

# Modulo 1 - Usuarios
# Entidade: Usuario (dois registros, um por usuario)
#

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
