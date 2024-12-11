from rest_framework import viewsets

from online_platform.models import Product, Contact, Provider
from online_platform.serializers import ProductSerializer, ContactSerializer, ProviderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD для работы с продуктами"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactViewSer(viewsets.ModelViewSet):
    """CRUD для работы с контактами"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """CRUD для работы с поставщиками"""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
