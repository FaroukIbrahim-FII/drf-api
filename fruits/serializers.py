from rest_framework import serializers
from .models import Fruit


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'owner', 'timestamp', 'discription']
        model = Fruit
