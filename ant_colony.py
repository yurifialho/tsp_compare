import acopy
import networkx as nx
class AntColonySolver:

    def __init__(self, graph, numExecution=30, debug=False):
        self.bestSolutions = []
        self.bestDistances = []
        self.executionTimes = []
        self.originalGraph = graph
        self.initiate(graph)
        self.numExecution = numExecution
        self.debug = debug

    def initiate(self, matrix):
        nodes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i != j and matrix[i][j] != []:
                    nodes.append((i, j, {'weight': matrix[i][j]}))
        self.nodes = nx.Graph(nodes)
        
    def run(self):
        for i in range(self.numExecution):
            solver = acopy.Solver(rho=.03, q=1)
            time = acopy.plugins.Timer()
            solver.add_plugin(time)
            colony = acopy.Colony(alpha=1, beta=3)
            tour = solver.solve(self.nodes, colony, limit=100)
            self.bestSolutions.append(tour.nodes)
            self.bestDistances.append(tour.cost)
            self.executionTimes.append(time.duration)
            if self.debug:
                print(f"[{i}] Execution Time: {time.duration}; Distance: {tour.cost}; ", end=" ")
                print(tour.nodes)
    
    def getSolutions(self):
        return self.bestSolutions, self.bestDistances, self.executionTimes