from matriz import ExampleMatrix
from ant_colony import AntColonySolver

example = ExampleMatrix()

#Execute the example path with exact algorithm, it will execute 30 times by default 

#TODO Initialy i do it with Dinamic Programming by cannot run, because it's very slow,
#  and now i will do it with branch an bound algorithm to gain some time.

#Execute the example path with ant colony algorithm, it will execute 30 times by default
acoSolver = AntColonySolver(example.getMatrix())
acoSolver.run()
bestSolutions, bestDistances, executionsTime = acoSolver.getSolutions() 

for i in range(len(bestSolutions)):
    print(f"[{i}] Execution Time: {executionsTime[i]}; Distance: {bestDistances[i]}; ", end=" ")
    print(bestSolutions[i])


