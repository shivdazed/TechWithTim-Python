class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.length() == p.length()

    def __add__(self, p):
        return self.x + p.x, self.y + p.y

    def __sub__(self, p):
        return self.x - p.x, self.y - p.y

    def __mul__(self, p):
        return self.x*p.x + self.y*p.y

    def __str__(self):
        return self.x, self.y


p1 = Point(3, 4)
p2 = Point(4, 4)
p3 = Point(5, 6)
p4 = Point(6, 3)
p5 = p1 + p2
p6 = p4 - p3
p7 = p3 * p4


print(p5,p6,p7)
print(p2 > p1)
print(p3 >= p2)
print(p3 < p1)
print(p4 <= p4)
print(p3 == p2)