from django.urls import path

from . import views

app_name = 'demo'

urlpatterns = [
    path('',views.index, name='home'),
    # path('products',views.products),
    # path('products-by-category/<slug:slug>',views.products_by_category),
    # path('products/stock',views.product_stocks),
    path('category',views.CategoryList.as_view(),name='category'),
    path('category/<uuid:uid>',views.CategoryDetail.as_view(),name='category-detail'),
    path('products',views.ProductList.as_view(), name='products'),
    path('products/<slug:slug>', views.ProductDetail.as_view(), name='product-detail'),
    path('product-by-category/<str:name>', views.ProductByCategoryList.as_view(), name='product-by-category')

]