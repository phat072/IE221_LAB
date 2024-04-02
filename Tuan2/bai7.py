class Candidate:
    def __init__(self) -> None:
        maso = ''
        hoten = ''
        ngaysinh = ''
        toan = 0.0
        van = 0.0
        anh = 0.0
        
    def nhap(self):
        self.maso = input("Nhap ma so: ")
        self.hoten = input("Nhap ho ten: ") 
        self.ngaysinh = input("Nhap ngay thang nam sinh: ")
        self.toan = float(input("Nhap diem toan: "))
        self.van = float(input("Nhap diem van: "))
        self.anh = float(input("Nhap diem anh: "))

    def xuat(self):
        print("Ma so: ", self.maso)
        print("Ho ten: ", self.hoten)
        print("Ngay sinh: ", self.ngaysinh)
        print("Diem toan: ", self.toan)
        print("Diem van: ", self.van)
        print("Diem anh: ", self.anh)
        
    def testCandidate(self):
        if self.toan + self.van + self.anh > 15:
            return True
        else:
            return False