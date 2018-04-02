import numpy as np
from KeyGen import get_keys

def encrypt(open_key, r):
    n = 2**r - 1
    Hpub, t = open_key
    Hpub_T = Hpub.transpose()
    vectors = []
    cipher = {}
    for i in range(n):
        vectors.append([1 if j==i else 0 for j in range(n)])
    for m in vectors:
        c = np.dot(m, Hpub_T)%2
        cipher['{}'.format(m)] = c
    return cipher

def decrypt(cipher, priv_key):


if __name__ == '__main__':
    r = int(input())
    open_key, priv_key = get_keys(r)
    cipher_ = encrypt(open_key, r)
    for key in cipher_:
        print('{} --> {}'.format(key, cipher_[key]))