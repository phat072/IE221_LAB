class Book:
    def __init__(self, title="", author="", price=0):
        self.title = title
        self.author = author
        self.price = price

    def print_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

    def calculate_total(self, quantity):
        return self.price * quantity

