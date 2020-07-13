from point import *

def dot_product(p1, p2):
    return ((p1.x*p2.x)+(p1.y*p2.y))  

def perp(vector):
    return Point(x=-vector.y,y=vector.x)
