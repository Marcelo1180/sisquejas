# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 22:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('queja', 'Queja'), ('reclamo', 'Reclamo'), ('sugerencia', 'Sugerencia'), ('solicitud_informacion', 'Solicitud de Informacion')], max_length=50)),
                ('comentario', models.TextField(verbose_name='Comentario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]