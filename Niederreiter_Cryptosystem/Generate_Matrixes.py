import numpy as np

def get_check_matrix(r, n):
    H_T = []
    for i in range(1, n + 1):
        H_T.append([int(elem) for elem in '{:0{}b}'.format(i, r)])
    return np.array(H_T, dtype='uint8').transpose()

def get_S_matrix(n, k):
    while True:
        S_matrix = np.random.random_integers(0, 1, (n-k, n-k))
        if np.linalg.matrix_rank(S_matrix) == n - k:
            return S_matrix.astype('uint8')

def get_P_matrix(n):
    P_matrix = []
    indexes = np.random.permutation(n)
    for index in indexes:
        P_matrix.append([1 if i == index else 0 for i in range(n)])
    return np.array(P_matrix, dtype='uint8')