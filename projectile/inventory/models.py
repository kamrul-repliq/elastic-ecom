"""Models for our inventory app."""
from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField

from uuid import uuid4

class BaseModelWithUUID(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract=True

class Category(BaseModelWithUUID):
    name = models.CharField(
        max_length=100,
        verbose_name=_("category name"),
        help_text=_("Format: required, max=100")
        )
    
    slug = AutoSlugField(populate_from='name')


    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
class Product(BaseModelWithUUID):
    """Models for product"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = name = models.CharField(max_length=100)
    slug = slug = AutoSlugField(populate_from='name')
    web_id = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    buying_price = models.PositiveIntegerField(default=0)
    selling_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class ProductInventory(BaseModelWithUUID):
    sku = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("stock keeping unit"),
        help_text=_("Format: required, unique, max=20")
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        verbose_name=_("universal product code"),
        help_text=_("Format: required, unique, max=12")
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_list')

class Stock(BaseModelWithUUID):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_list')
    stock = models.IntegerField(default=0)
