import json

from Customer import Customer
from CustomerDataAccess import CustomerDataAccess
from flask import Flask, request

app = Flask(__name__)
dao = CustomerDataAccess(r'C:\sqlite\customer.db')


@app.route("/")
def home():
    print('hi')
    return '''
        <html>
            Ready!
        </html>
    '''


@app.route('/customers', methods=['GET', 'POST'])
def get_or_post_customer():
    if request.method == 'GET':
        customers = dao.print_all_customers()
        return json.dumps(customers)
    if request.method == 'POST':
        customer_data = request.get_json()
        new_customer = Customer(id=None, name=customer_data["name"], address=customer_data["address"])
        return dao.post_customer(new_customer)


@app.route('/customers/<int:customer_id>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def get_customer_by_id(customer_id):
    if request.method == 'GET':
        customer = dao.get_customer_by_id(customer_id)
        return json.dumps(customer)
    if request.method == 'PUT':
        customer = request.get_json()
        return dao.put_customer(customer)
    if request.method == 'DELETE':
        return dao.delete_customer(customer_id)
    if request.method == 'PATCH':
        customer = request.get_json()
        return dao.patch_customer(customer)


app.run()
