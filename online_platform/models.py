from django.db import models

from users.models import NULLABLE


class Supplier(models.Model):
    """Модель поставщика"""

    SUPPLIER_TYPES = (
        ("factory", "Завод"),
        ("retail_network", "Розничная сеть"),
        ("Individual_entrepreneur", "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=250, verbose_name="Название поставщика")
    supplier = models.ForeignKey(
        "self", **NULLABLE, on_delete=models.SET_NULL, verbose_name="Поставщик"
    )
    supplier_type = models.CharField(
        max_length=40, choices=SUPPLIER_TYPES, verbose_name="Тип поставщика"
    )
    level = models.IntegerField(verbose_name="Уровень в иерархии")
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        **NULLABLE,
        default=0,
        verbose_name="Задолжность перед поставщиком",
    )
    creation_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    def __str__(self):
        return f"{self.name} {self.supplier_type} {self.level}"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        ordering = ("name",)


class Product(models.Model):
    """Модель продукта"""

    title = models.CharField(max_length=250, verbose_name="Название")
    model = models.CharField(max_length=250, **NULLABLE, verbose_name="Модель")
    release_date = models.DateTimeField(**NULLABLE, verbose_name="Дата выхода на рынок")
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, **NULLABLE, verbose_name="Поставщик"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("title",)


class Contract(models.Model):
    """Модель контакта"""

    email = models.EmailField(max_length=80, verbose_name="Email")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=150, verbose_name="Город")
    street = models.CharField(max_length=150, **NULLABLE, verbose_name="Улица")
    house_number = models.PositiveIntegerField(**NULLABLE, verbose_name="Номер дома")
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, **NULLABLE, verbose_name="Поставщик"
    )

    def __str__(self):
        return f"{self.email} {self.city} {self.country}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = (
            "city",
            "country",
        )
