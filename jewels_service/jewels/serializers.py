from rest_framework import serializers
from .models import Jewel


class JewelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jewel
        fields = '__all__'
