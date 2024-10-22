import factory
from factory.fuzzy import FuzzyChoice
from models import Product

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('word')
    category = FuzzyChoice(choices=['Electronics', 'Furniture', 'Clothing', 'Toys'])
    price = factory.Faker('random_number', digits=5)
    available = FuzzyChoice(choices=[True, False])
