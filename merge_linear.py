from collections import deque
from collinear_test import CollinearTest

def merge_linear(P, hull):
    test = CollinearTest(P, hull[0], hull[1])

    if test == "POSITIVE":
        hull = [P, hull[0], hull[1]]
        return hull

    if test == "NEGATIVE":
        hull = [P, hull[1], hull[0]]
        return hull

    if test == "COLLINEAR_LEFT":
        hull = [P, hull[1]]
        return hull

    if test == "COLLINEAR_RIGHT":
        hull = [hull[0], P]
        return hull

    if test == "COLLINEAR_CONTAIN":
        return hull
    
    

