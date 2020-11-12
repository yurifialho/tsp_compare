from matriz import ExampleMatrix
from ant_colony import AntColonySolver
from tsp_lp import LinearProgrammSolver

example = ExampleMatrix()

#Execute the example path with exact algorithm, it will execute 30 times by default 

with open('tsp_lp.log', 'w') as f:
    for exeN in range(30):
        lp = LinearProgrammSolver()
        executionsTime, bestDistance, bestSolution = lp.run(example.getTriangularMatrix())
        print(f"[{exeN}] Execution Time: {executionsTime}; Distance: {bestDistance}; ", end=" ", file=f)
        print(bestSolution,file=f)

#Execute the example path with ant colony algorithm, it will execute 30 times by default
acoSolver = AntColonySolver(example.getMatrix(), 2, True)
acoSolver.run()
bestSolutions, bestDistances, executionsTime = acoSolver.getSolutions() 

with open('aco_solver.log', 'w') as f:
    for i in range(len(bestSolutions)):
        print(f"[{i}] Execution Time: {executionsTime[i]}; Distance: {bestDistances[i]}; ", end=" ", file=f)
        print(bestSolutions[i], file=f)


