# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
from itertools import permutations
from matriz import ExampleMatrix
V = 29

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

	# store all vertex apart from source vertex 
	vertex = [] 
	for i in range(V): 
		if i != s: 
			vertex.append(i) 

	# store minimum weight Hamiltonian Cycle 
	min_path = maxsize 
	next_permutation=permutations(vertex)
	for i in next_permutation:
		print(i)
		# store current Path weight(cost) 
		current_pathweight = 0

		# compute current path weight 
		k = s 
		for j in i: 
			current_pathweight += graph[k][j] 
			k = j 
		current_pathweight += graph[k][s] 

		# update minimum 
		min_path = min(min_path, current_pathweight)
		#print(min_path)
		
	return min_path 


# Driver Code 
if __name__ == "__main__": 

    e = ExampleMatrix()
    graph = e.getMatrix()
    s = 0
    print(travellingSalesmanProblem(graph, s))