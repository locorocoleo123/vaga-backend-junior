from rest_framework import serializers
from . import models

class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Clube
        fields = "__all__"

