from rest_framework.generics import ListAPIView
from demo.serializers import ProductSerializer
from inventory.documents import ProductDocument

class ProductSearch(ListAPIView):
    serializer_class = ProductSerializer
    search_document = ProductDocument
    
    
    def get_queryset(self):
        queryset = self.search_document.search().filter('match', name=self.kwargs['name'])
        return queryset
