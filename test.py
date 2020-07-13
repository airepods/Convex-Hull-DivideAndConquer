from get_hull import getHull, findConvexHull
from collections import deque
import numpy as np
import matplotlib.pyplot as plt


n=500
points = [tuple(i) for i in np.random.random_integers(-100000, 100000, size=(n,2))]

print(*points)

l = list(set([i for i in points])) 
l.sort(key=lambda p: (p[0], p[1]))

x_p, y_p = zip(*l)

hull = findConvexHull(n, points)

print(*hull)

hull.append(hull[0])

x = list()
y = list()
for p in hull:
    x.append(p.x)
    y.append(p.y)

plt.title("n="+str(n))
plt.scatter(x_p,y_p,c="blue")
plt.plot(x,y,c="red",linewidth=1)
plt.show()




