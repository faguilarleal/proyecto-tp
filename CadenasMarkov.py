
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

P2 = np.linalg.matrix_power(P,2)

prob_menganita = 0
prob_chispudito = 0
for i in range(8):
    for j in range(8):
        if j == 0:
            prob_menganita += P2[i][j]
        if j == 6:
            prob_chispudito += P2[i][j]

print(f"Probabilidad de que gane Menganita: {prob_menganita/8}")
print(f"Probabilidad de que gane Chispudito: {prob_chispudito/8}")

