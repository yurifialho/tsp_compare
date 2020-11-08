#https://pypi.org/project/ACO-Pants/
import numpy as np
import pants
import math
import random

from matriz import ExampleMatrix

e = ExampleMatrix()

distances = e.getMatrix()
nodes = []
for i in range(len(distances)):
    d = [distances[i][j] for j in range(len(distances[i]))]
    nodes.append((i, d))

def distance(a, b):
    return a[1][b[0]]

world = pants.World(nodes, distance)
solver = pants.Solver()
#solution = solver.solve(world)
solutions = solver.solutions(world)

#print(solution.distance)
# Nodes visited in order
#for i in solution.tour:
#    print(i[0], end=",")

#print(solution.path)    # Edges taken in order
#1 28 6 12 9 26 3 29 5 21 2 20 10 4 15 18 14 17 22 11 19 25 7 23 8 27 16 13 24

best = float("inf")
for solution in solutions:
  assert solution.distance < best
  best = solution.distance
  tour = solution.tour
print(best)
for i in solution.tour:
    print(i[0], end=",")