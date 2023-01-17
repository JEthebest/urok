from .models import Category, Qa
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'title', 
        )
   

class QaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Qa
        fields = (
            'question',
            'answer',
            'category'
        )