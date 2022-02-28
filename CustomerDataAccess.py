import sqlite3

from Customer import Customer


# DAO - Data Access Object
class CustomerDataAccess:

    def __init__(self, file_path):
        self.con = sqlite3.connect(file_path)
        self.cursor = self.con.cursor()

    def print_all_customers(self):
        customers_ls = []
        self.cursor.execute("select * from customers")
        customers = self.cursor.fetchall()
        for customer in customers:
            customers_ls.append(Customer(id_=customer[0], name=customer[1], address=customer[2]))
        return_ls = [customer.__dict__ for customer in customers_ls]
        return return_ls

    def get_customer_by_id(self, id):
        self.cursor.execute(f"select * from customers where id = {id}")
        customer = self.cursor.fetchall()
        if customer:
            print(customer)
            selected_customer = Customer(id_=customer[0][0], name=customer[0][1], city=customer[0][2])
            return selected_customer.__dict__
        else:
            return []

        # def get_customer_by_id(self, id):
        #     self.cursor.execute("select * from customer where " +
        #                         f" id = {id}")
        #     customer = None
        #     for row in self.cursor:
        #         customer = Customer(row[0], row[1], row[2], row[3], row[4])
        #     return customer

    def delete_customer(self, customer_id):
        self.cursor.execute(f"delete from customer where id = {customer_id} ")
        self.con.commit()

    def post_customer(self, customer):
        self.cursor.execute(f'INSERT INTO customer VALUES ("{customer.id}", ' +
                            f' "{customer.name}", "{customer.address}")')
        self.con.commit()

    def put_customer(self, customer):
        # if not exist --> add
        # 2. if exist, update fields with given data
        # 3.           missing fields will have None value
        self.cursor.execute(f"select * from customers where id = {customer.id}")
        founded_customer = self.cursor.fetchall()
        if not founded_customer:
            self.cursor.execute(f'INSERT INTO customer VALUES ("{customer.id}", ' +
                                f' "{customer.name}", "{customer.address}")')
            self.con.commit()
        else:
            self.cursor.execute(f'UPDATE customer SET  id = {customer.id},  name = "{customer.name}",  ' +
                                f'address = "{customer.address}" where id = {founded_customer.id} ')
            self.con.commit()

    def patch_customer(self, customer):
        # 1. if not exist --> return
        # 2. if exist, update fields with given data
        # 3.           missing fields will remain the same
        self.cursor.execute(f"select * from customers where id = {customer.id}")
        founded_customer = self.cursor.fetchall()
        if customer.name == None:
            customer.name = founded_customer.name
        if customer.address == None:
            customer.address = founded_customer.address
        self.cursor.execute(f'UPDATE customer SET  id = {customer.id},  name = "{customer.name}",  ' +
                            f'address = "{customer.address}" where id = {founded_customer.id} ')
        self.con.commit()


# db = r'C:\sqlite\customer.db'
# a = CustomerDataAccess(db)
