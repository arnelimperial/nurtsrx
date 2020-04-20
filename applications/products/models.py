from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='products',
        related_query_name='product'
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(blank=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name




