from rest_framework import serializers

from online_platform.models import Provider, Product, Contact


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор модели контактов"""

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели продуктов"""

    class Meta:
        model = Product
        fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
    """Сериализатор модели поставщиков"""

    contacts = ContactSerializer(source="contact_set", many=True, read_only=True)
    products = ProductSerializer(source="product_set", many=True, read_only=True)

    def update(self, instance, validated_data):
        """Запрет на изменение задолжности"""
        validated_data.pop("debt", None)
        return super().update(instance, validated_data)

    class Meta:
        model = Provider
        fields = "__all__"
