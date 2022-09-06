import numpy as np
from time import time

# Resolving knight problem on a NxN chessboard, N > 4
# L : Array of chessboard
# k : actual number of the knight
# x,y : actual position of the knight
# N : size of the chessboard
# AES : Algorithme à essais successifs
# While moving, the knight will go from 1 to N*N


def AES(L, N, x, y, k):
    if k > N * N:
        return True
    else:
        deltas = [
            [1, 2],
            [1, -2],
            [-1, 2],
            [-1, -2],
            [2, 1],
            [2, -1],
            [-2, 1],
            [-2, -1],
        ]
        for delta in deltas:
            x1 = x + delta[0]
            y1 = y + delta[1]
            if L[x1 + 2, y1 + 2] == -1:
                L[x1 + 2, y1 + 2] = k
                if AES(L, N, x1, y1, k + 1):
                    print(L)
                    return False
                else:
                    L[x1 + 2, y1 + 2] = -1
                    global backs
                    backs += 1
        return False


if __name__ == "__main__":
    N = int(input())
    L = np.full((N + 4, N + 4), 0)
    L[2:-2, 2:-2] = -1
    x0, y0 = map(int, input("Coordonnées de départ au format x y: ").split())
    L[x0 + 2][y0 + 2] = 1
    next = 2
    backs = 0
    t0 = time()
    if AES(L, N, x0, y0, next):
        print(L)
    else:
        print("Echec / Pas de nouvelle solution")
    print("Nombre de retours arrière : ", backs)
    print("Temps d'exécution : ", time() - t0)
