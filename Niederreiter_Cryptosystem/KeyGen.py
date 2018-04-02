import numpy as np

def transpose(M):
    l = len(M)
    for j in range(len(M[0])):
        M.append([M[i][j] for i in range(l)])
    for i in range(l): M.pop(0)

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

def get_keys(r):
    n = 2**r - 1
    k = 2**r - 1 - r
    t = 1
    H = get_check_matrix(r, n)
    S = get_S_matrix(n, k)
    P = get_P_matrix(n)
    Hpub = np.dot(S, H)
    np.dot(Hpub, P, out=Hpub)
    Hpub %= 2
    open_key = (Hpub, t)
    inv_P = np.linalg.inv(P).astype('uint8')
    inv_S = (np.linalg.inv(S)%2).astype('uint8')
    priv_key = (inv_S, H, inv_P)
    return (open_key, priv_key)