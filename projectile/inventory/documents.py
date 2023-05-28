"""Documents for our models ElasticSearch."""

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Category,Product, Stock


@registry.register_document
class ProductDocument(Document):

    category = fields.ObjectField(properties={
        'uid': fields.TextField(),
        'name': fields.TextField(),
    })
    
    class Index:
        name = "products"

    class Django:
        model = Product

        fields = ['uid','name','selling_price']

        related_models = [Category]
    
    def get_queryset(self):
        return super(ProductDocument, self).get_queryset().select_related(
            'category'
        )
    

# @registry.register_document
# class ProductWithStockDocument(Document):

#     stock_list = fields.NestedField(properties = {
#         "uid": fields.TextField(),
#         "product_id": fields.IntegerField(),
#         "stock": fields.IntegerField(),
#     })

#     class Index:
#         name = "product_stock"

#     class Django:
#         model = Product
#         fields = [
#             "uid","name","selling_price"
#         ]

#         related_models = [Stock]
#     def get_queryset(self):
#         return super(ProductWithStockDocument, self).get_queryset().prefetch_related(
#             "stock_list",
#         )
