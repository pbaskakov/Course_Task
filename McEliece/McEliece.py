import sys
sys.path.append('C:\\Users\\Admin\\source\\repos\\Course_Task\\Niederreiter_Cryptosystem')
from Generate_Matrixes import get_gen_matrix, get_S_matrix, get_P_matrix
import numpy as np
from random import sample

def encrypt(a, open_key, error_vectors):
    #e = sample(error_vectors, 1)[0]
    e = [0,0,0,1,0,0,0]
    b = (np.dot(a, open_key) + e).astype('uint8') % 2
    return b

if __name__ == '__main__':
    r = 3
    n = 2**r - 1
    k = 2**r - 1 - r
    G = np.array([[1,0,0,0,1,1,1],
                  [0,1,0,0,1,1,0],
                  [0,0,1,0,1,0,1],
                  [0,0,0,1,0,1,1]], dtype='uint8')

    S = np.array([[1,0,1,0],
                  [0,1,1,1],
                  [1,0,0,0],
                  [0,0,1,1]], dtype='uint8')

    P = np.array([[0,0,0,0,1,0,0],
                  [0,0,1,0,0,0,0],
                  [0,0,0,0,0,0,1],
                  [0,0,0,1,0,0,0],
                  [1,0,0,0,0,0,0],
                  [0,1,0,0,0,0,0],
                  [0,0,0,0,0,1,0]], dtype='uint8')


    #G = get_gen_matrix(r, n, k)
    #S = get_S_matrix(k)
    #P = get_P_matrix(n)
    #priv_key = (S, P)
    open_key = np.dot(S, G) % 2
    np.dot(open_key, P, out=open_key)
    open_key %= 2
    error_vectors = [[0 for i in range(n)]]
    error_vectors.extend([[1 if j == i else 0 for j in range(n)] for i in range(n)])
    a = [1,1,1,0]
    print(encrypt(a, open_key, error_vectors))