import random


def play(N, game, coord, human):
    color = False
    end = False
    while not end:
        if color == human:
            place_human(N, game, coord, color)
        else:
            place_random(N, game, coord, color)
        end = win(N, game, color)
        if not end:
            color = not color
    return color


def place_random(N, game, coord, color):
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


def place_human(N, game, coord, color):
    x, y = -1, -1
    print("\n")
    for k in game:
        print(k)
    if len(coord[color]) == N:
        print("Il va falloir déplacer un pion.")
        while not ((x, y) in coord[2]):
            x, y = map(
                int, input("Coordonnées du nouveau pion au format x y : ").split()
            )
    else:
        while not ((x, y) in coord[2]):
            x, y = map(int, input("Coordonnées du pion au format x y : ").split())
    game[x][y] = color
    coord[color].append((x, y))
    coord[2].remove((x, y))
    if len(coord[color]) == N + 1:
        x1, y1 = -1, -1
        while not ((x1, y1) in coord[color]):
            x1, y1 = map(
                int, input("Coordonnées du pion à retirer au format x y : ").split()
            )
        game[x1][y1] = float("inf")
        coord[color].remove((x1, y1))
        coord[2].append((x1, y1))


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
    human = -1
    while not (human == 0 or human == 1):
        human = int(input("\nBlancs (0) ou Noirs (1) ? "))
    print(
        "\nLes Noirs ont gagné !\n"
        if play(N, game, coord, human)
        else "\nLes Blancs ont gagné !\n"
    )
    for k in game:
        print(k)


if __name__ == "__main__":
    initialize(int(input("N = ? ")))
