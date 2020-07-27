from rest_framework import serializers
from podnety.models import Podnet


class PodnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podnet
        fields = ['id', 'firstName', 'lastName', 'adress', 'description', 'image', 'uploadDate']
