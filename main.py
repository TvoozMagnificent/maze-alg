X = 50
Y = 1000

from collections import defaultdict
from random import choice

def decrease(n): return n - 1 if n > 0 else n + 1

def default(point):
    x, y = point
    if x == y == 0: return (0, 0)
    if y == 0: return (decrease(x), y)
    return (x, decrease(y))

origin = (0, 0)
neighbors = {}

def origin_shift(origin, neighbors):
    dx, dy = choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
    ox, oy = origin
    nx, ny = ox + dx, oy + dy
    new = (nx, ny)
    neighbors[origin] = neighbors[new] = new
    return new, neighbors

for _ in range(Y): origin, neighbors = origin_shift(origin, neighbors)

# draw the path in matplotlib
import matplotlib.pyplot as plt

for x1 in range(-X, X+1):
    for y1 in range(-X, X+1):
        try: x2, y2 = neighbors[(x1, y1)]
        except Exception as e: x2, y2 = default((x1, y1)); print(e)
        plt.plot([x1, x2], [y1, y2], 'b-')

plt.show()
