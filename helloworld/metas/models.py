from django.db import models

# Create your models here.

# Modulo 3 - Metas financeiras
# Entidade: MetaFinanceira
#
# class MetaFinanceira(models.Model):
#     id -> automatico
#     nome -> ex: "Entrada do imovel"
#     valor_total -> ?
#     valor_atual -> ?
#     data_limite -> ?
#     status -> ?
#
# Pergunta que a API vai responder:
# "Estamos no ritmo certo para bater a meta?"
# -> compara valor_atual x valor_total x tempo restante ate data_limite
