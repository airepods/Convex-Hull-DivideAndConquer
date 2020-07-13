class Point:
    def __init__(self, x=0, y=0, point=None):
        if point != None:
            self.x = point.x
            self.y = point.y
        else:
            self.x = x
            self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, p2):
        x = self.x + p2.x
        y = self.y + p2.y
        return Point(x, y)

    def __sub__(self, p2):
        x = self.x - p2.x
        y = self.y - p2.y
        return Point(x, y)
    
    def __mul__(self, p2):
        x = self.x * p2.x
        y = self.y * p2.y
        return Point(x, y)
