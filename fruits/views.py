from django.shortcuts import render
from rest_framework import generics
from .serializers import FruitSerializer
from .models import Fruit


# CR methods in the list view
class FruitListView(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

# RUD methods in the detailed view
class FruitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

