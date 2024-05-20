import numpy as np

# Define the states for easy reference
states = ["HHH", "THT", "Start", "H","T", "HH", "TH"]

# Initialize the transition matrix
P = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0.5, 0.5, 0, 0],
    [0, 0, 0, 0, 0.5, 0.5, 0],
    [0, 0, 0, 0, 0.5, 0, 0.5],
    [0.5, 0, 0, 0, 0.5, 0, 0],
    [0, 0.5, 0, 0, 0, 0.5, 0]
])

# Define the indices of the absorbing states
HHH_index = states.index("HHH")
THT_index = states.index("THT")

# Define the submatrix Q of non-absorbing states
non_absorbing_indices = [i for i in range(len(states)) if i not in {HHH_index, THT_index}]
T = P[np.ix_(non_absorbing_indices, non_absorbing_indices)]
# Define the submatrix R of transitions to absorbing states
M = P[np.ix_(non_absorbing_indices, [HHH_index, THT_index])]
# Identity matrix for the size of Q
I = np.eye(T.shape[0])

# Fundamental matrix N = (I - Q)^-1
N = np.linalg.inv(I - T)

# Calculate the absorbing probabilities B = NR
B = N @ M

P_HHH_first = B[0, 0]
P_THT_first = B[0, 1]

print(f"Probability of HHH appearing first: {P_HHH_first}")
print(f"Probability of THT appearing first: {P_THT_first}")

