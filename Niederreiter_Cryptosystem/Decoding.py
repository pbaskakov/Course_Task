import numpy as np
from math import log
from Generate_Matrixes import get_check_matrix

def decode(c, H, n):
    H_T = H.transpose()
    s = np.dot(c, H_T) % 2
    if 1 not in s:
        b = s.copy()
    else:
        s = s.astype('U1')
        i = int(''.join(s), 2)
        s = s.astype('uint8')
        e = np.array([1 if j == i-1 else 0 for j in range(n)], dtype='uint8')
        b = (c - e) % 2
    indexes = [i for i in range(int(log(n,2)) + 1)]
    a = np.delete(b, indexes)
    return a

if __name__ == '__main__':
    pass