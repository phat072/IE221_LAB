class Bread:
    def __init__(self, id, name, type, country, expiry_date, price):
        self.id = id
        self.name = name
        self.type = type
        self.country = country
        self.expiry_date = expiry_date
        self.price = price

    def print_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Type: {self.type}, Country: {self.country}, Expiry date: {self.expiry_date}, Price: {self.price}")

    def calculate_price(self, quantity):
        return self.price * quantity


class NoBread(Bread):
    def __init__(self, id, name, type, country, expiry_date):
        super().__init__(id, name, type, country, expiry_date, 5000)
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)   


class MomBread(Bread):
    def __init__(self, id, name, type, country, expiry_date):
        super().__init__(id, name, type, country, expiry_date, 20000)
    def calculate_price(self, quantity):
        return super().calculate_price(quantity)    