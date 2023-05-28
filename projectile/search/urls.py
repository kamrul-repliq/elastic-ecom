"""URL mappings for search."""

from django.urls import path

from search import views

urlpatterns = [
    path('/products/<str:name>', views.ProductSearch.as_view(),name='search'),
]