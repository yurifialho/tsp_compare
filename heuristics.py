# Usage https://pypi.org/project/python-tsp/
import numpy as np
from python_tsp.heuristics import solve_tsp_local_search
from matriz import ExampleMatrix

e = ExampleMatrix()
permutation, distance = solve_tsp_local_search(np.array(e.getMatrix()))
print(permutation)