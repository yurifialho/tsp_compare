import tsp
import numpy as np
import time

class LinearProgrammSolver():

    def run(self, matriz):
        r = range(len(matriz))
        # Dicionário de distâncias
        dist = {}
        for i in r:
            dist[(i,i)] = 0
            for j, valor in enumerate(matriz[i]):
                dist[(i,j+i+1)] = valor
                dist[(j+i+1,i)] = valor

        s = range(len(matriz)+1)
        startTime = time.time() 
        result = tsp.tsp(s, dist)
        execTime = time.time()-startTime
        tsp_lista = result[1]
        tsp_resultante = [x+1 for x in tsp_lista]
        return execTime, int(result[0]), tsp_resultante        
        
