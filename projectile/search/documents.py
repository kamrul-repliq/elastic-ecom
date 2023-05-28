# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry

# from inventory.models import Category,Product, Stock

# @registry.register_document
# class ProductStockDocument(Document):
#     # stock_list = fields.NestedField(properties = {
#     #     "uid": fields.TextField(),
#     #     "product_uid": fields.TextField(),
#     #     "stock": fields.IntegerField(),
#     # })
#     class Index:
#         name="productstock"
    
#     class Django:
#         model = Product
#         fields = [
#             'uid',
#             'name',
#             'selling_price',
#         ]
#         # related_models =[Stock]
    
#     # def get_queryset(self):
#     #     return super(ProductStockDocument, self).get_queryset().prefetch_related(
#     #         "stock_list",
#     #     )
