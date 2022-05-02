from re import search
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer
from .filters import ProductsFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend,)
    # filter_backends = [SearchFilter]
    # search_fields = ['description', ]
    
    filterset_fields = ['products', 'address', 'product_name' ]
    filterset_class= ProductsFilter
    pagination_class = LimitOffsetPagination
