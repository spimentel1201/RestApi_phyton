from flask import Flask, jsonify, request
from flask.wrappers import Request

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def hello_world():
    return "Hello world!"

from products import products
@app.route('/test')
def ping():
    return jsonify({"message": "Hola bro"})

@app.route('/products', methods={'GET'})
def getProducts():
    return jsonify({"products": products,"message": "Product's List"})

@app.route('/products/<string:product_id>')
def getProduct(product_id):
    print(product_id)
    productsFound = [product for product in products if product['id'] == product_id]
    if (len(productsFound)>0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message":"Product not found"})

@app.route('/products/', methods=['POST'])
def addProduct():
    new_product = {
        "id" : request.json('id'),
        "name" : request.json['name'],
        "price" : request.json['price'],
        "quantity" : request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message":"Product added succesfully","products": products})

@app.route('/products/<string:product_id>',methods=['PUT'])
def editProduct(product_id):
    productFound = [product for product in products if product['id'] == product_id]
    if(len(productFound)>0):
        productFound[0]['id'] = request.json['id']
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product updated successfully.",
            "product": productFound[0]
        })
    return jsonify({
        "message": "Product not found.",
        "product": productFound[0]
    })

@app.route('/products/<string:product_id>',methods=['DELETE'])
def deleteProduct(product_id):
    productsFound = [product for product in products if product['id'] == product_id]
    if(len(productsFound)>0):
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product deleted.",
            "products": products
        })
    return jsonify({"message": "Product not found."})
if __name__ == '__main__':
    app.run('127.0.0.1',debug=True,port=5000)
