from django.contrib import admin
from nurtsrx.applications.products.models import (
    Product, Manufacturer
)

product_models = Product, Manufacturer
admin.site.register(product_models)
