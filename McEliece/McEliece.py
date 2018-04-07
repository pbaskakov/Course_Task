import sys
sys.path.append('C:\\Users\\Admin\\source\\repos\\Course_Task\\Niederreiter_Cryptosystem')
from Generate_Matrixes import *
import numpy as np
from random import sample
from Decoding import decode

def encrypt(a, open_key, error_vectors):
    #e = sample(error_vectors, 1)[0]
    e = [0,0,0,1,0,0,0]
    b = (np.dot(a, open_key) + e).astype('uint8') % 2
    return b

def decrypt(b, priv_key, H):
    inv_S = np.linalg.inv(priv_key[0]).astype('uint8') % 2
    inv_P = np.linalg.inv(priv_key[1]).astype('uint8') % 2
    b_ = np.dot(b, inv_P) % 2
    a_ = decode(b_, H, H.shape[1])
    a = np.dot(a_, inv_S) % 2
    return a

if __name__ == '__main__':
    r = 3
    n = 2**r - 1
    k = 2**r - 1 - r

    #G = np.array([[1,0,0,0,1,1,1],
    #              [0,1,0,0,1,1,0],
    #              [0,0,1,0,1,0,1],
    #              [0,0,0,1,0,1,1]], dtype='uint8')

    #S = np.array([[1,0,1,0],
    #              [0,1,1,1],
    #              [1,0,0,0],
    #              [0,0,1,1]], dtype='uint8')

    #P = np.array([[0,0,0,0,1,0,0],
    #              [0,0,1,0,0,0,0],
    #              [0,0,0,0,0,0,1],
    #              [0,0,0,1,0,0,0],
    #              [1,0,0,0,0,0,0],
    #              [0,1,0,0,0,0,0],
    #              [0,0,0,0,0,1,0]], dtype='uint8')

    H = get_check_matrix(r, n)
    G = get_gen_matrix(H, r, k)
    S = get_S_matrix(k)
    P = get_P_matrix(n)
    priv_key = (S, P)
    open_key = np.dot(S, G) % 2
    np.dot(open_key, P, out=open_key)
    open_key %= 2
    error_vectors = [[0 for i in range(n)]]
    error_vectors.extend([[1 if j == i else 0 for j in range(n)] for i in range(n)])
    a = [1,1,1,0]
    b = encrypt(a, open_key, error_vectors)
    print(b)
    a = decrypt(b, priv_key, H)
    print(a)
  