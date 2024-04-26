import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('category_data.json', encoding='utf-8') as file:
            category_data = json.load(file)
            return category_data

    @staticmethod
    def json_read_products():
        with open('product_data.json', encoding='utf-8') as file:
            product_data = json.load(file)
            return product_data

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products()():
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)