
# Menganita y Chispudito juegan con una moneda balanceada (no cargada). El juego consiste en que cada uno escoge una combinación de caras y cruces de largo 3 y empiezan a tirar la moneda. 
# La primera persona que obtenga su combinación al tirar la moneda gana (la moneda se tira hasta que alguno de los dos gane). 
# Menganita selecciona CCC, mientras que Chispudito selecciona XCX. 
  
# Para ayudarle a Menganita, debe calcular la probabilidad de que cada uno de ellos gane.

import numpy as np


# Definimos la matriz de transición
print("PROBLEMA RESOLVIENDOLO UTILIZANDO CADENAS DE MARKOV")

P = np.array([[1,0, 0,  0,  0,  0,  0,  0 ],
            [0.5, 0, 0,  0,  0.5, 0,  0,  0 ],
            [0, 0,  0,  0.5, 0,  0,  0,  0.5],
            [0, 0.5, 0,  0,  0,  0,  0.5, 0 ],
            [0, 0,  0.5, 0,  0.5,  0, 0,  0 ],
            [0, 0.5, 0,  0,  0,  0,  0.5, 0 ],
            [0, 0,  0,  0,  0,  0,  1,  0, ],
            [0, 0,  0,  0.5, 0,  0,  0,  0.5]])

#Submatriz de estados transitorios (los que no son CCC Y XCX) 
Q = P[np.ix_([1,2,3,4,5,7], [1,2,3,4,5,7])]
# print("\n\n\n\n\n")
# print(Q)

#Submatriz de estados absorbentes (los que sí son CCC Y XCX) 
R = P[np.ix_([1,2,3,4,5,7], [0,6])]
# print("\n\n\n\n\n")
# print(R)

#Matriz fundamental que se crea con la inversa de la resta de la submatriz Q a la matriz identidad 6x6. (N:=(I−Q)^−1)
N = np.linalg.inv(np.eye(6) - Q)
# print("\n\n\n\n\n")
# print(N)

#Producto escalar entre la matriz fundamental (N) y la sumatriz de estados absorbentes
B = np.dot(N, R)
# print("\n\n\n\n\n")
# print(B)
# print("\n\n\n\n\n")

prob_menganita = B[0, 0]
prob_chispudito = B[0,1]

print(f"Probabilidad de que gane Menganita: {prob_menganita}")
print(f"Probabilidad de que gane Chispudito: {prob_chispudito}")

