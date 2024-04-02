class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.calcPerimeter()}")
        print(f"Area: {self.calcArea()}")

    def calcPerimeter(self):
        return 2 * (self.length + self.width)

    def calcArea(self):
        return self.length * self.width


class Parallelpipe(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.calcArea() * self.height