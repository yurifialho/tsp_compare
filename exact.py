# Usage https://pypi.org/project/python-tsp/
# https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante
import numpy as np
from python_tsp.exact import solve_tsp_brute_force #solve_tsp_dynamic_programming
from matriz import ExampleMatrix

e = ExampleMatrix()
permutation, distance = solve_tsp_brute_force(np.array(e.getMatrix())) #solve_tsp_dynamic_programming(np.array(e.getMatrix()))
print(permutation)