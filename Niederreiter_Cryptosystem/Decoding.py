import numpy as np
from math import log
from Generate_Matrixes import get_check_matrix

def decode(s, n):
    #H_T = H.transpose()
    #print(c)
    #print(H_T)
    #s = np.dot(c, H_T) % 2
    if 1 not in s:
        b = s.copy()
    else:
        s = s.astype('U1')
        i = int(''.join(s), 2)
        s = s.astype('uint8')
        e = np.array([1 if j == i-1 else 0 for j in range(n)], dtype='uint8')
        b = (s - e) % 2
    indexes = [i for i in range(int(log(n,2)) + 1)]
    a = np.delete(b, indexes)
    return a

if __name__ == '__main__':
    H = get_check_matrix(3, 7)
    c = np.array([1,1,0,1,1,1,1], dtype='uint8')
    print(decode(c, 7, H))