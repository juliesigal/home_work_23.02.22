from Customers import Customers

class DbRepo:
    def __init__(self, local_session):
        self.local_session = local_session

    def get_customer_by_id(self, id_to_get):
        return self.local_session.query(Customers).get(id_to_get)

    def get_all_customers(self):
        return self.local_session.query(Customers).all()

    def post_customer(self, customer):
        self.local_session.add(customer)
        self.local_session.commit()

    def delete_customer(self, id_column_name, id_to_remove):
        self.local_session.query(Customers).filter(id_column_name == id_to_remove).delete(synchronize_session=False)
        self.local_session.commit()

    def put_by_id(self, id_column_name, id_to_update, data):
        existing_object = self.local_session.query(Customers).filter(id_column_name == id_to_update)
        if not existing_object:
            self.local_session.add(existing_object)
        existing_object.update(data)
        self.local_session.commit()

    def patch_by_id(self, id_column_name, id_to_update, data):
        existing_object = self.local_session.query(Customers).filter(id_column_name == id_to_update)
        existing_object.update(data)
        self.local_session.commit()

