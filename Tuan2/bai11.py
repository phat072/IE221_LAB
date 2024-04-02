class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def translate(self, dx, dy):
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)
        self.p3.translate(dx, dy)

    def centroid(self):
        x = (self.p1.x + self.p2.x + self.p3.x) / 3
        y = (self.p1.y + self.p2.y + self.p3.y) / 3
        return Point(x, y)


class Polygon:
    def __init__(self, points):
        self.points = points

    def translate(self, dx, dy):
        for point in self.points:
            point.translate(dx, dy)