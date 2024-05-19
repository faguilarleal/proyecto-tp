
# Menganita y Chispudito juegan con una moneda balanceada (no cargada). El juego consiste en que cada uno escoge una combinación de caras y cruces de largo 3 y empiezan a tirar la moneda. 
# La primera persona que obtenga su combinación al tirar la moneda gana (la moneda se tira hasta que alguno de los dos gane). 
# Menganita selecciona CCC, mientras que Chispudito selecciona XCX. 
  
# Para ayudarle a Menganita, debe calcular la probabilidad de que cada uno de ellos gane.

import numpy as np


# Definimos la matriz de transición

P = np.array([[1, 0.5, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0.5, 0, 0.5, 0, 0], 
              [0, 0, 0, 0, 0.5, 0, 0, 0], 
              [0, 0, 0.5, 0, 0, 0, 0, 0.5], 
              [0, 0.5, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0.5, 0, 0, 0], 
              [0, 0, 0, 0.5, 0, 0.5, 1, 0], 
              [0, 0, 0.5, 0, 0, 0, 0, 0.5]])

# Definimos el vector de estado inicial






