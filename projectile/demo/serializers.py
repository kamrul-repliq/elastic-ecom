from rest_framework import serializers
from django.urls import reverse

from inventory.models import (
    Category,
    Product,
    Stock
)

class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self,obj):
        request = self.context.get('request')
        url = reverse('demo:category-detail', args=[obj.uid])
        return f'<a href="{url}">View category</a>'
    class Meta:
        model = Category
        fields = ('uid','name',"url")


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    profit = serializers.IntegerField(read_only=True)
    class Meta:
        model = Product
        fields = ("uid","name","slug","selling_price","profit","is_active","description","category","stock_list")


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fileds = "__all__"