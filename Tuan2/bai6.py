class SoPhuc:
    def __init__(self, thuc=1, ao=1):
        self.thuc = thuc
        self.ao = ao

    def add(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    def subtract(self, other):
        return SoPhuc(self.thuc - other.thuc, self.ao - other.ao)

    def multiply(self, other):
        thuc = self.thuc * other.thuc - self.ao * other.ao
        ao = self.thuc * other.ao + self.ao * other.thuc
        return SoPhuc(thuc, ao)

    def divide(self, other):
        thuc = (self.thuc * other.thuc + self.ao * other.ao) / (other.thuc**2 + other.ao**2)
        ao = (other.thuc * self.ao - self.thuc * other.ao) / (other.thuc**2 + other.ao**2)
        return SoPhuc(thuc, ao)

    def __str__(self):
        return f"{self.thuc} + {self.ao}i"

