from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from online_platform.models import Product, Contact, Provider
from online_platform.permissions import IsActiveStaff
from online_platform.serializers import (
    ProductSerializer,
    ContactSerializer,
    ProviderSerializer,
)
from online_platform.services import CountryFilter


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD для работы с продуктами"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveStaff,)


class ContactViewSet(viewsets.ModelViewSet):
    """CRUD для работы с контактами"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsActiveStaff,)


class ProviderViewSet(viewsets.ModelViewSet):
    """CRUD для работы с поставщиками"""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CountryFilter
    permission_classes = (IsActiveStaff,)
