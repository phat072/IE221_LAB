class SoNguyen:
    def __init__(self, value=0):
        self.value = value

    def add(self, other=0):
        return self.value + other.value

    def subtract(self, other):
        return self.value - other.value

    def multiply(self, other):
        return self.value * other.value

    def divide(self, other):
        if other.value == 0:
            return "Error: Division by zero"
        return self.value / other.value

