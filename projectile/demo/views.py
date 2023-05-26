from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import F,When,Case,Prefetch
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from inventory.models import (
    Category,
    Product,
    Stock,
)
import json
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    StockSerializer
)


from inventory import models

# Create your views here.

class CategoryList(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
    lookup_field = "uid"

class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter().select_related('category').prefetch_related('stock_list')
    print(str(queryset.query))

class ProductByCategoryList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs["name"]
        queryset = Product.objects.filter(category__name__icontains=category).prefetch_related('stock_list')
        return queryset

class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    stocks = Stock.objects.filter(is_active=True).only("uid","product_id")
    queryset = Product.objects.filter(
    ).prefetch_related(
        Prefetch(
        "stock_list",
        queryset=stocks
        )
    ).annotate(profit=F('selling_price')-F('buying_price'))
    lookup_field = "slug"

def index(request):
    data = models.Category.objects.only("uid","name","is_active")
    print(str(data.query))
    json_data = serialize('json', data)
    return JsonResponse(json_data, safe=False)

def products(request):
    products = models.Product.objects.all()
    json_products = serialize('json',products)
    return JsonResponse(json_products, safe=False)

def products_by_category(request,slug):
    category = models.Category.objects.get(slug=slug)
    products = models.Product.objects.filter(category__name=category.name)

    json_products = serialize('json',products)
    return JsonResponse(json_products, safe=False)

def product_stocks(request):
    products = models.Product.objects.filter().prefetch_related('stock_list')
    json_products = serialize('json',products)
    return JsonResponse(json_products, safe=False)
