from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Qa
from .serializers import CategorySerializer,QaSerializer
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QaViewSet(ModelViewSet):
    queryset = Qa.objects.all()
    serializer_class = QaSerializer
