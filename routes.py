from flask import Flask, jsonify, request
from models import Product

app = Flask(__name__)

@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.find_by_id(id)
    return jsonify(product.serialize()), 200 if product else 404

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.find_by_id(id)
    if product:
        product.update(data)
        return jsonify(product.serialize()), 200
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.find_by_id(id)
    if product:
        product.delete()
        return '', 204
    return jsonify({'message': 'Product not found'}), 404

@app.route('/products', methods=['GET'])
def list_products():
    products = Product.all()
    return jsonify([p.serialize() for p in products]), 200

@app.route('/products', methods=['GET'])
def find_by_name():
    name = request.args.get('name')
    product = Product.find_by_name(name)
    return jsonify(product.serialize()), 200 if product else 404

@app.route('/products', methods=['GET'])
def find_by_category():
    category = request.args.get('category')
    products = Product.find_by_category(category)
    return jsonify([p.serialize() for p in products]), 200

@app.route('/products', methods=['GET'])
def find_by_availability():
    available = request.args.get('available', 'true').lower() == 'true'
    products = Product.find_by_availability(available)
    return jsonify([p.serialize() for p in products]), 200
