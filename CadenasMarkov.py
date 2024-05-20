import numpy as np

# Estados 
states = ["HHH", "THT", "Start", "H","T", "HH", "TH"]

# Matriz de transición
P = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0.5, 0.5, 0, 0],
    [0, 0, 0, 0, 0.5, 0.5, 0],
    [0, 0, 0, 0, 0.5, 0, 0.5],
    [0.5, 0, 0, 0, 0.5, 0, 0],
    [0, 0.5, 0, 0, 0, 0.5, 0]
])

# Indices de los estados absorbentes
HHH_index = states.index("HHH")
THT_index = states.index("THT")

# Define la submatriz T de los estados no absorbentes
non_absorbing_indices = [i for i in range(len(states)) if i not in {HHH_index, THT_index}]
T = P[np.ix_(non_absorbing_indices, non_absorbing_indices)]
# Define la matriz M de transición a los estados absorbentes
M = P[np.ix_(non_absorbing_indices, [HHH_index, THT_index])]
# Matriz identidad del tamaño de T
I = np.eye(T.shape[0])

# Matriz fundamental N = (I - T)^-1
N = np.linalg.inv(I - T)

# Calcula la probabilidades absorbentes B = NM
B = N @ M

P_HHH_first = B[0, 0]
P_THT_first = B[0, 1]

print(f"Probabilidad de que Menganita gane: {P_HHH_first}")
print(f"Probabilidad de que Chispudito gane: {P_THT_first}")

