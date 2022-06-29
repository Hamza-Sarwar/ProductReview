from dataclasses import fields
from .models import Product, CustomerReportRecord, Category, User
from rest_framework import serializers
from django.utils import timezone


class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReportRecord

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']

class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (timezone.now() - obj.date_joined).days