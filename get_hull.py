from collections import deque
from merge import merge
from point import *

def getHull(i0, i1, points, hull):
    quantity = (i1 - i0) + 1
    if quantity > 1:
        mid = int((i0 + i1)/2)

        lHull = deque()
        rHull = deque()

        getHull(i0, mid, points, lHull)
        getHull(mid+1, i1, points, rHull)

        hull = merge(lHull, rHull, hull)
    else:
        hull.append(points[i0])


def removeDuplicates(l): 
    points = deque([])
    l = list(set([i for i in l])) 
    for x, y in l:
        points.append(Point(x,y))
    
    return points

def findConvexHull(n, points):
    points = removeDuplicates(points)
    points_f = sorted(points, key=lambda p: (p.x, p.y))
    n = len(points_f)
    hull = deque([])
    getHull(0, n-1, points_f, hull)
    return hull





