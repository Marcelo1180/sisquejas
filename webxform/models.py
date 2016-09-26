from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


TIPO_COMENTARIO = (
    ('queja', 'Queja'),
    ('reclamo', 'Reclamo'),
    ('sugerencia', 'Sugerencia'),
    ('solicitud_informacion', 'Solicitud de Informacion'),
)

class Comentario(models.Model):
    tipo = models.CharField(max_length=50, choices=TIPO_COMENTARIO)
    comentario = models.TextField(verbose_name='Comentario')
    usuario = models.ForeignKey(User)q
