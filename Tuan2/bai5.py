from math import gcd

class PhanSo:
    def __init__(self, tu_so=1, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def rut_gon(self):
        ucln = gcd(self.tu_so, self.mau_so)
        return PhanSo(self.tu_so // ucln, self.mau_so // ucln)

    def add(self, other):
        tu_so = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau_so = self.mau_so * other.mau_so
        return PhanSo(tu_so, mau_so).rut_gon()

    def subtract(self, other):
        tu_so = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau_so = self.mau_so * other.mau_so
        return PhanSo(tu_so, mau_so).rut_gon()

    def multiply(self, other):
        tu_so = self.tu_so * other.tu_so
        mau_so = self.mau_so * other.mau_so
        return PhanSo(tu_so, mau_so).rut_gon()

    def divide(self, other):
        tu_so = self.tu_so * other.mau_so
        mau_so = self.mau_so * other.tu_so
        return PhanSo(tu_so, mau_so).rut_gon()

    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"

