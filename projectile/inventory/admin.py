from django.contrib import admin
from inventory.models import Category, Product,Stock

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("uid","name","slug","created_at","updated_at","is_active")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("uid","name","slug","buying_price","selling_price","created_at","updated_at","is_active")


class StockAdmin(admin.ModelAdmin):
    list_display = ("uid","product","stock","created_at","updated_at","is_active")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)