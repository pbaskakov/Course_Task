import numpy as np
from Generate_Matrixes import *
def encrypt(Hpub, n):
    Hpub_T = Hpub.transpose()
    cipher_vectors = {}
    for i in range(n):
        c = Hpub_T[i]
        cipher_vectors['{}'.format([1 if j == i else 0 for j in range(n)])] = c
    return cipher_vectors

def decrypt(cipher, H, P, inv_S, n):
    inv_S_T = inv_S.transpose()
    H_T = H.transpose().tolist()
    P_T_inv = np.linalg.inv(P.transpose()).astype('uint8') % 2
    plain_vectors = {}
    for c in cipher.values():
        s = np.dot(c, inv_S_T) % 2
        index_1 = H_T.index(s.tolist())
        m_ = np.array([1 if i == index_1 else 0 for i in range(n)], dtype='uint8')
        m = np.dot(m_, P_T_inv) % 2
        plain_vectors['{}'.format(c)] = m
    return plain_vectors

if __name__ == '__main__':
    r = 3
    n = 2**r - 1
    k = 2**r - 1 - r
    H = get_check_matrix(r, n)
    S = get_S_matrix(n-k)
    P = get_P_matrix(n)
    Hpub = np.dot(S, H) % 2
    Hpub = np.dot(Hpub, P) % 2
    inv_P = np.linalg.inv(P).astype('uint8') % 2
    inv_S = np.linalg.inv(S).astype('uint8') % 2
    cipher = encrypt(Hpub, n)
    for key in cipher:
        print('{} --> {}'.format(key, cipher[key]))
    print('__________________________________________')
    plain = decrypt(cipher, H, P, inv_S, n)
    for key in plain:
        print('{} --> {}'.format(key, plain[key]))