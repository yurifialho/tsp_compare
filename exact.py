# Usage https://pypi.org/project/python-tsp/
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
from matriz import ExampleMatrix

e = ExampleMatrix()
permutation, distance = solve_tsp_dynamic_programming(np.array(e.getMatrix()))
print(permutation)