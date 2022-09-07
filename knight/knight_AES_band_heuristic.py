import numpy as np
from time import time

# Resolving knight problem on a NxN chessboard, N > 4
# L : Array of chessboard
# k : actual number of the knight
# x,y : actual position of the knight
# N : size of the chessboard
# AES : Algorithme à essais successifs
# While moving, the knight will go from 1 to N*N


def init_neighbours(L, N):
    global deltas
    neighbours = L.copy()
    for i in range(N):
        for j in range(N):
            free_neighbours = 0
            for delta in deltas:
                x1 = i + delta[0]
                y1 = j + delta[1]
                if L[x1 + 2, y1 + 2] == -1:
                    free_neighbours += 1
            neighbours[i + 2, j + 2] = free_neighbours
    return neighbours


def update_neighbours(x, y):
    global deltas
    global neighbours
    for delta in deltas:
        x1 = x + delta[0]
        y1 = y + delta[1]
        if neighbours[x1 + 2, y1 + 2] > 0:
            neighbours[x1 + 2, y1 + 2] -= 1


def back_neighbours(x, y):
    global deltas
    global neighbours
    for delta in deltas:
        x1 = x + delta[0]
        y1 = y + delta[1]
        if neighbours[x1 + 2, y1 + 2] > -1:
            neighbours[x1 + 2, y1 + 2] += 1


def find_best_free_neighbours(x, y):
    global deltas
    global neighbours
    global L

    def find_best_neighbours_value(x, y):
        min_k = 9
        for delta in deltas:
            x1 = x + delta[0]
            y1 = y + delta[1]
            if neighbours[x1 + 2, y1 + 2] < min_k and L[x1 + 2, y1 + 2] == -1:
                min_k = neighbours[x1 + 2, y1 + 2]
        return min_k

    def find_best_neighbours(x, y):
        min_k = find_best_neighbours_value(x, y)
        best_neighbours = []
        for delta in deltas:
            x1 = x + delta[0]
            y1 = y + delta[1]
            if neighbours[x1 + 2, y1 + 2] == min_k and L[x1 + 2, y1 + 2] == -1:
                best_neighbours.append((x1, y1))
        return best_neighbours

    return find_best_neighbours(x, y)


def AES(L, N, x, y, k):
    if k > N * N:
        return True
    else:
        best_neighbours = find_best_free_neighbours(x, y)
        for neighbour in best_neighbours:
            x1 = neighbour[0]
            y1 = neighbour[1]
            L[x1 + 2, y1 + 2] = k
            update_neighbours(x1, y1)
            if AES(L, N, x1, y1, k + 1):
                return True
            else:
                L[x1 + 2, y1 + 2] = -1
                back_neighbours(x1, y1)
                global backs
                backs += 1
        return False


if __name__ == "__main__":
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
    N = int(input())
    L = np.full((N + 4, N + 4), N * N + 1)
    L[2:-2, 2:-2] = -1
    neighbours = init_neighbours(L, N)
    x0, y0 = map(int, input("Coordonnées de départ au format x y: ").split())
    L[x0 + 2, y0 + 2] = 1
    next = 2
    backs = 0
    t0 = time()
    if AES(L, N, x0, y0, next):
        print(L)
    else:
        print("Echec (et pas mat)")
    print("Nombre de retours arrière : ", backs)
    print("Temps d'exécution : ", time() - t0)
