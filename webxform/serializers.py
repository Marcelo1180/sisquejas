#!/usr/bin/python
# -*- coding: utf8 -*-
from models import Comentario
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
