import random


def play(N, game, coord):
    color = False
    end = False
    while not end:
        place(N, game, coord, color)
        end = win(N, game, color)
        if not end:
            color = not color
    return color


def place(N, game, coord, color):
    i, j = -1, -1
    if len(coord[color]) == N:
        rd = random.randint(0, N - 1)
        i, j = coord[color][rd]
    found = False
    while not found:
        x, y = random.randint(0, N - 1), random.randint(0, N - 1)
        if game[x][y] == float("inf"):
            game[x][y] = color
            coord[color].append((x, y))
            coord[2].remove((x, y))
            if i >= 0:
                coord[color].remove((i, j))
                coord[2].append((i, j))
                game[i][j] = float("inf")
            found = True


def win(N, game, color):
    for i in range(len(game)):
        S = sum(game[i])
        if S == N * color:
            return True
        S = sum([game[k][i] for k in range(N)])
        if S == N * color:
            return True
    S = sum([game[i][i] for i in range(N)])
    if S == N * color:
        return True
    S = sum([game[i][N - i - 1] for i in range(N)])
    if S == N * color:
        return True
    return False


def initialize(N):
    game = [[float("inf") for i in range(N)] for j in range(N)]
    coord = [[], [], []]
    for i in range(N):
        for j in range(N):
            coord[2].append((i, j))
    print("Noirs" if play(N, game, coord) else "Blancs")


if __name__ == "__main__":
    initialize(int(input("N = ? ")))
