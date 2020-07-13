from point import *
from linear_algebra import dot_product, perp
from enum import Enum
  
class Position(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    COLLINEAR_LEFT = 3
    COLLINEAR_RIGHT = 4
    COLLINEAR_CONTAIN = 5

def CollinearTest(P, Q0, Q1):
    # Creating vectors
    D = Point(point=Q1-Q0)
    A = Point(point=P-Q0)
    N = perp(D)

    NdA = dot_product(N,A)
    if NdA > 0:
        return Position.POSITIVE.name
    if NdA < 0:
        return Position.NEGATIVE.name
    
    DdA = dot_product(D,A)
    if DdA < 0:
        return Position.COLLINEAR_LEFT.name
    if DdA > dot_product(D,D):
        return Position.COLLINEAR_RIGHT.name
    
    return Position.COLLINEAR_CONTAIN.name


