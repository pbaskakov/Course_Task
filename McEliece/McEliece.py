import sys
sys.path.append('C:\\Users\\Admin\\source\\repos\\Course_Task\\Niederreiter_Cryptosystem')
from Generate_Matrixes import get_gen_matrix, get_S_matrix, get_P_matrix
import numpy as np
from itertools import permutations

def encrypt(n, k, open_key):
    error_vectors = []

if __name__ == '__main__':
    r = 3
    n = 2**r - 1
    k = 2**r - 1 - r
    G = get_gen_matrix(r, n, k)
    S = get_S_matrix(k)
    P = get_P_matrix(n)
    priv_key = (S, P)
    open_key = np.dot(S, G) % 2
    np.dot(open_key, P, out=open_key)
    open_key %= 2
    print(open_key)