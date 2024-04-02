class Circle:
    def __init__(self, a, b, r) -> None:
        self.a = a
        self.b = b
        self.r = r
    
    def calc_area(self):
        return 3.14 * self.r**2
    
    def calc_perimeter(self):
        return 2 * 3.14 * self.r
    
    def testBelongs(self, A_x, A_y):
        dist = ((A_x-self.a)**2 + (A_y-self.b)**2)**0.5
        if dist == self.r:
            return True
        else: 
            return False