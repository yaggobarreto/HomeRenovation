from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

# Modulo Reforma
# Entidade: ReformaItem


class ReformaItem(models.Model):
    class Status(models.TextChoices):
        PLANEJAMENTO = 'planejamento', 'Planejamento'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        CONCLUIDO = 'concluido', 'Concluído'

    nome = models.CharField(max_length=250)
    categoria = models.CharField(max_length=100)
    custo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    custo_real = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, 
        choices=Status.choices,
        default=Status.PLANEJAMENTO,
    )
    prioridade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    data_estimavel = models.DateField()

    def __str__(self):
        return self.nome