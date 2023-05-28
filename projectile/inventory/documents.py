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
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Category):
            return related_instance.product_set.all()

@registry.register_document
class ProductWithStockDocument(Document):
    category = fields.ObjectField(properties={
        'uid': fields.TextField(),
        'name': fields.TextField(),
    })
    stock_list = fields.NestedField(properties = {
        "uid": fields.TextField(),
        "product_id": fields.KeywordField(),
        "stock": fields.IntegerField(),
    })

    class Index:
        name = "product_stock"

    class Django:
        model = Product
        fields = [
            "uid","name","selling_price"
        ]

        related_models = [Stock, Category]
    def get_queryset(self):
        return super(ProductWithStockDocument, self).get_queryset().prefetch_related(
            "stock_list",
        )
    
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, Stock):
            return related_instance.product
        elif isinstance(related_instance, Category):
            return related_instance.product_set.all()
