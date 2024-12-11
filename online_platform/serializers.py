from rest_framework import serializers

from online_platform.models import Provider, Product


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор модели контактов"""

    class Meta:
        model = Provider
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продуктов"""

    class Meta:
        model = Product
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    """Сериализатор модели поставщиков"""

    contacts = ContactSerializer(source='contact_set', many=True, read_only=True)
    products = ProductSerializer(source='product_set', many=True, read_only=True)

    class Meta:
        model = Provider
        fields = '__all__'
