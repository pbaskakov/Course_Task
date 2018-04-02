def transpose(M):
    pass

def get_check_matrix(r, n):
    H_T = []
    for i in range(1, n + 1):
        H_T.append([int(elem) for elem in '{:0{}b}'.format(i, r)])
    return H_T

if __name__ == '__main__':
    r = int(input())
    n = 2**r - 1
    k = 2**r - 1 - r
    H_T = get_check_matrix(r, n)
    for row in H_T:
        print(row)
