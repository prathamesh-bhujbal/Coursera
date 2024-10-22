import unittest
from models import Product
from factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def test_create_product(self):
        product = ProductFactory()
        self.assertIsNotNone(product)

    def test_read_product(self):
        product = ProductFactory()
        fetched = Product.find_by_name(product.name)
        self.assertEqual(fetched.name, product.name)

    def test_update_product(self):
        product = ProductFactory()
        product.price = 2000
        product.save()
        self.assertEqual(Product.find_by_name(product.name).price, 2000)

    def test_delete_product(self):
        product = ProductFactory()
        product.delete()
        self.assertIsNone(Product.find_by_name(product.name))

    def test_list_all_products(self):
        products = Product.all()
        self.assertGreaterEqual(len(products), 1)

    def test_find_by_name(self):
        product = ProductFactory()
        result = Product.find_by_name(product.name)
        self.assertEqual(result.name, product.name)

    def test_find_by_category(self):
        product = ProductFactory(category='Electronics')
        result = Product.find_by_category('Electronics')
        self.assertIn(product, result)

    def test_find_by_availability(self):
        product = ProductFactory(available=True)
        result = Product.find_by_availability(True)
        self.assertIn(product, result)
