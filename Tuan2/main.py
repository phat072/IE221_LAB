import bai1
import bai2
import bai3
import bai4
import bai5
import bai6
import bai7
import bai8


def cau1():
    # Sử dụng lớp Book
    book = bai1.Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    book.print_info()
    quantity = int(input("Enter the quantity of books you want to buy: "))
    total = book.calculate_total(quantity)
    print(f"The total price for {quantity} books is: {total}")

def cau2():
    c = bai2.Circle(0,0,3)
    print("chu vi la: ",c.calc_area())
    print("dien tich la: ",c.calc_perimeter())
    A_x, A_y = map(float, input().split())
    if c.testBelongs(A_x, A_y):
        print("diem A thuoc duong tron")
    else:
        print("diem A khong thuoc duong tron")

def cau3():
    d = bai3.Dice()
    n = int(input('Nhập số lần tung xúc xắc: '))
    log = []
    for i in range(n):
        d.roll()
        log.append(d.num)
    print(log)
    
    for i in range (1, 7):
        print('Xác suất của mặt ', i, 'là: ', log.count(i)/n)

def cau4():
    # Nhập vào hai số nguyên và thực hiện các phép toán
    num1 = bai4.SoNguyen(int(input("Enter the first integer: ")))
    num2 = bai4.SoNguyen(int(input("Enter the second integer: ")))

    print("Addition result: ", num1.add(num2))
    print("Subtraction result: ", num1.subtract(num2))
    print("Multiplication result: ", num1.multiply(num2))
    print("Division result: ", num1.divide(num2))

def cau5():
    # Nhập vào hai phân số và thực hiện các phép toán
    tu_so1 = int(input("Tu so 1: "))
    mau_so1 = int(input("Mau so 1: "))
    tu_so2 = int(input("Tu so 2: "))
    mau_so2 = int(input("Mau so 2: "))

    phan_so1 = bai5.PhanSo(tu_so1, mau_so1)
    phan_so2 = bai5.PhanSo(tu_so2, mau_so2)

    print("Addition result: ", phan_so1.add(phan_so2))
    print("Subtraction result: ", phan_so1.subtract(phan_so2))
    print("Multiplication result: ", phan_so1.multiply(phan_so2))
    print("Division result: ", phan_so1.divide(phan_so2))

def cau6():
    # Nhập vào hai số phức và thực hiện các phép toán
    thuc1 = float(input("Nhap phan thuc so thu nhat: "))
    ao1 = float(input("Nhap phan ao so thu nhat: "))
    thuc2 = float(input("Nhap phan thuc so thu hai: "))
    ao2 = float(input("Nhap phan ao so thu hai: "))

    so_phuc1 = bai6.SoPhuc(thuc1, ao1)
    so_phuc2 = bai6.SoPhuc(thuc2, ao2)

    print("Addition result: ", so_phuc1.add(so_phuc2))
    print("Subtraction result: ", so_phuc1.subtract(so_phuc2))
    print("Multiplication result: ", so_phuc1.multiply(so_phuc2))
    print("Division result: ", so_phuc1.divide(so_phuc2))

def cau7():
    n = int(input("Nhap so luong thi sinh: "))
    l = []
    for i in range(n):
        cand = bai7.Candidate()
        print("Nhap thong tin thi sinh thu ", i+1, ':')
        cand.nhap()
        l.append(cand)
    print("Danh sach thi sinh thoa dieu kien: ")
    for i in range(n):
        if l[i].testCandidate() == True:
            l[i].xuat()

def cau8():
    # Test the String class
    s1 = bai8.String("Hello")
    s2 = bai8.String(" World")
    print("String 1: ", s1)
    print("String 2: ", s2)
    print("Length of String 1: ", s1.length())
    print("Concatenation: ", s1.concatenate(s2))
    print("Reverse of String 1: ", s1.reverse())

import bai9
def cau9():
     # Create a Rectangle object
    rect = bai9.Rectangle(10, 5)
    print("Rectangle:")
    rect.display()

    # Create a Parallelpipe object
    pipe = bai9.Parallelpipe(10, 5, 3)
    print("\nParallelpipe:")
    pipe.display()
    print(f"Volume: {pipe.volume()}")

import bai10
def cau10():
     # Create a Student object
    student = bai10.Student("CaPhat", 20)
    student.displayStudent()

import bai11

def cau11():
    p = bai11.Point(3, 5)
    print(p.get_point())
    p.translate(7, 10)
    print(p.get_point())

    t = bai11.Triangle(bai11.Point(0, 0), bai11.Point(1, 0), bai11.Point(0, 1))
    print(t.centroid().get_point())
    t.translate(1, 1)
    print(t.centroid().get_point())

    poly = bai11.Polygon([bai11.Point(0, 0), bai11.Point(1, 0), bai11.Point(1, 1), bai11.Point(0, 1)])
    for point in poly.points:
        print(point.get_point())
    poly.translate(1, 1)
    for point in poly.points:
        print(point.get_point())
    
import bai12
def cau12():
     # Create a NoBread object
    no_bread = bai12.NoBread("1", "No Bread", "Type1", "Country1", "2022-12-31")
    no_bread.print_info()
    print(no_bread.calculate_price(10))

    # Create a MomBread object
    mom_bread = bai12.MomBread("2", "Mom Bread", "Type2", "Country2", "2022-12-31")
    mom_bread.print_info()
    print(mom_bread.calculate_price(10))
    

def main():
    # cau1()
    # cau2()
    # cau3()
    # cau4()
    # cau5()
    # cau6()
    # cau7()
    # cau8() Cau 8 is not working
    # cau9()
    # cau10()
    # cau11()
    cau12()
    
    
if __name__ == "__main__":
    main()