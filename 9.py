import numpy as np 

vetor_coluna = [2, 3, 5, 7, 9]

matriz = [[0.7, 0.7, 0.5, 0.2, 0.5],
          [0.7, 0.0, 0.4, 0.3, 0.6],
          [0.5, 0.4, 0.2, 0.6, 0.4],
          [0.2, 0.3, 0.6, 0.9, 0.2],
          [0.5, 0.6, 0.4, 0.2, 0.1]]

print(sum(np.dot(matriz, vetor_coluna)))


