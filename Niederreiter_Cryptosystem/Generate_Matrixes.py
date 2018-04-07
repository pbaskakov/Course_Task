import numpy as np

def get_check_matrix(r, n):
    H_T = []
    for i in range(1, n + 1):
        H_T.append([int(elem) for elem in '{:0{}b}'.format(i, r)])
    return np.array(H_T, dtype='uint8').transpose()

def get_S_matrix(dim):
    while True:
        S_matrix = np.random.random_integers(0, 1, (dim, dim))
        if np.linalg.det(S_matrix) % 2 == 1:
            return S_matrix.astype('uint8')

def get_P_matrix(n):
    P_matrix = []
    indexes = np.random.permutation(n)
    for index in indexes:
        P_matrix.append([1 if i == index else 0 for i in range(n)])
    return np.array(P_matrix, dtype='uint8')

def get_gen_matrix(H, r, k):
    H_T_list = H.transpose().tolist()
    for i in range(r):
        H_T_list.pop(H_T_list.index([1 if j == i else 0 for j in range(r)]))
    P_part = np.array(H_T_list, dtype='uint8')
    E_part = np.eye(k, dtype='uint8')
    return np.hstack((E_part, P_part))

if __name__ == '__main__':
    pass