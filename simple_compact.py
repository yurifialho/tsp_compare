"""Example that solves the Traveling Salesman Problem using the simple compact
formulation presented in Miller, C.E., Tucker, A.W and Zemlin, R.A. "Integer
Programming Formulation of Traveling Salesman Problems". Journal of the ACM
7(4). 1960."""

from itertools import product
from sys import stdout as out
from mip import Model, xsum, minimize, BINARY
from matriz import ExampleMatrix

# names of places to visit
places = [([i+1 for i in range(29)])]

# distances in an upper triangular matrix
e = ExampleMatrix()
dists = e.getTriangularMatrix()

# number of nodes and list of vertices
n, V = len(dists), set(range(len(dists)))

# distances matrix
c = [[0 if i == j
      else dists[i][j-i-1] if j > i
      else dists[j][i-j-1]
      for j in V] for i in V]

model = Model()

# binary variables indicating if arc (i,j) is used on the route or not
x = [[model.add_var(var_type=BINARY) for j in V] for i in V]

# continuous variable to prevent subtours: each city will have a
# different sequential id in the planned route except the first one
y = [model.add_var() for i in V]

# objective function: minimize the distance
model.objective = minimize(xsum(c[i][j]*x[i][j] for i in V for j in V))

# constraint : leave each city only once
for i in V:
    model += xsum(x[i][j] for j in V - {i}) == 1

# constraint : enter each city only once
for i in V:
    model += xsum(x[j][i] for j in V - {i}) == 1

# subtour elimination
for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        model += y[i] - (n+1)*x[i][j] >= y[j]-n

# optimizing
model.optimize()

# checking if a solution was found
if model.num_solutions:
    out.write('route with total distance %g found: %s'
              % (model.objective_value, places[0]))

# sanity tests
from mip import OptimizationStatus
assert model.status == OptimizationStatus.OPTIMAL
assert round(model.objective_value) == 547
model.check_optimization_results()