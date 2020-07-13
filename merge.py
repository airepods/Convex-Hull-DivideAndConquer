from collections import deque
from collinear_test import CollinearTest
from merge_linear import merge_linear


def getTangent(lHull, rHull, L, R):
    i = 0
    while(i<len(lHull)+len(rHull)):
        L1 = lHull[L]
        R0 = rHull[R]

        Lm1 = (L-1) % len(lHull)
        L0 = lHull[Lm1]
        test = CollinearTest(R0, L0, L1)
        if test == "NEGATIVE" or test == "COLLINEAR_LEFT":
            L = Lm1
            i+=1
            continue

        Rm1 = (R+1) % len(rHull)
        R1 = rHull[Rm1]
        test = CollinearTest(L1, R0, R1)
        if test == "NEGATIVE" or test == "COLLINEAR_LEFT":
            R = Rm1
            i+=1
            continue

        break
    return L, R

def merge(lHull, rHull, hull):
    if len(lHull) == 1 and len(rHull) == 1:
        hull.append(lHull[0])
        hull.append(rHull[0])
        return hull

    if len(lHull) == 1 and len(rHull) == 2:
        rHull = merge_linear(lHull[0], rHull)

        hull.clear()
        for j in range(len(rHull)):
            hull.append(rHull[j])

        return hull

    if len(lHull) == 2 and len(rHull) == 1:
        lHull = merge_linear(rHull[0], lHull)

        hull.clear()
        for j in range(len(lHull)):
            hull.append(lHull[j])
            
        return hull

    if len(lHull) == 2 and len(rHull) == 2:
        lHull = merge_linear(rHull[1], lHull)
        if len(lHull) == 2:
            lHull = merge_linear(rHull[0], lHull)

            hull.clear()
            for j in range(len(lHull)):
                hull.append(lHull[j])

            return hull
    
        rHull.pop()
    
    Lmax = lHull.index(max(lHull, key=lambda p: p.x))
    Rmin = rHull.index(min(rHull, key=lambda p: p.x))

    LLindex = Lmax
    LRindex = Rmin

    LLindex, LRindex = getTangent(lHull, rHull, LLindex, LRindex)

    ULindex = Lmax
    URindex = Rmin

    URindex, ULindex = getTangent(rHull, lHull, URindex, ULindex)

    tempHull = deque([])

    j = LRindex
    while j != URindex:
        tempHull.append(rHull[j]) 
        j = (j+1) % len(rHull)
    tempHull.append(rHull[j]) 

    k = ULindex
    while k != LLindex:
        tempHull.append(lHull[k]) 
        k = (k+1) % len(lHull)
    tempHull.append(lHull[k]) 

    hull.clear()
    while(len(tempHull) != 0):
        hull.append(tempHull[0])
        tempHull.popleft()

    return hull

