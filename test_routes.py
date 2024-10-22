import unittest
from service import app
from factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_read_product(self):
        product = ProductFactory()
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = ProductFactory()
        response = self.client.put(f'/products/{product.id}', json={'price': 2000})
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        product = ProductFactory()
        response = self.client.delete(f'/products/{product.id}')
        self.assertEqual(response.status_code, 204)

    def test_list_all_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_list_by_name(self):
        product = ProductFactory()
        response = self.client.get(f'/products?name={product.name}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_category(self):
        response = self.client.get('/products?category=Electronics')
        self.assertEqual(response.status_code, 200)

    def test_list_by_availability(self):
        response = self.client.get('/products?available=true')
        self.assertEqual(response.status_code, 200)
