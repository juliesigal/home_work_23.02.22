class Customer:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        return f'id = {self.id}, first name is {self.name}, address is {self.address}'

    def __repr__(self):
        return f'id = {self.id}, first name is {self.name}, address is {self.address}'