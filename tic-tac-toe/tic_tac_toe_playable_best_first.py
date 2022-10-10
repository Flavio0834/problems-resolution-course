def evaluation(N, game, coord, color, coordinates, delete):
    if not delete:
        NL1, NL2, NC1, NC2, ND11, ND12, ND21, ND22 = 1, 0, 1, 0, 1, 0, 1, 0
    else:
        NL1, NL2, NC1, NC2, ND11, ND12, ND21, ND22 = 0, 0, 0, 0, 0, 0, 0, 0
    f1, f2, f3, f4 = 1, 1, 1, 1
    ncolor = not color
    for player in coord[color]:
        if player[0] == coordinates[0]:
            NL1 += 1
        if player[1] == coordinates[1]:
            NC1 += 1
    for opponent in coord[ncolor]:
        if opponent[0] == coordinates[0]:
            NL2 += 1
        if opponent[1] == coordinates[1]:
            NC2 += 1
    if coordinates[0] == coordinates[1]:
        for i in range(N):
            if game[i][i] == color:
                ND11 += 1
            if game[i][i] == ncolor:
                ND12 += 1
    if coordinates[0] == N - coordinates[1] - 1:
        for i in range(N):
            if game[i][N - i - 1] == color:
                ND21 += 1
            if game[i][N - 1 - i] == ncolor:
                ND22 += 1
    if NL2 > NL1:
        f1 = -1
    if NL2 > 1:
        f1 *= 2
    if NC2 > NC1:
        f2 = -1
    if NC2 > 1:
        f1 *= 2
    if ND12 > ND11:
        f3 = -1
    if ND12 > 1:
        f1 *= 2
    if ND22 > ND21:
        f3 = -1
    if ND22 > 1:
        f4 *= 2
    return (
        (
            f1 * (NL2 - NL1) ** 2
            + f2 * (NC2 - NC1) ** 2
            + f3 * (ND12 - ND11) ** 2
            + f4 * (ND22 - ND21) ** 2
        )
        * abs(f1)
        * abs(f2)
        * max(abs(f3), abs(f4))
    )


def play(N, game, coord, human):
    color = False
    end = False
    while not end:
        if color == human:
            place_human(N, game, coord, color)
        else:
            place_best_first(N, game, coord, color)
        end = win(N, game, color)
        if not end:
            color = not color
    return color


def place_best_first(N, game, coord, color):
    i, j = -1, -1
    if len(coord[color]) == N:
        mini = 0
        minimums = []
        for case in coord[color]:
            g = evaluation(N, game, coord, color, case, True)
            if g > mini:
                mini = g
        for case in coord[color]:
            g = evaluation(N, game, coord, color, case, True)
            if g == mini:
                minimums.append(case)
        i, j = minimums[0]
    found = False
    while not found:
        maxi = 0
        maximums = []
        for case in coord[2]:
            g = evaluation(N, game, coord, color, case, False)
            if g > maxi:
                maxi = g
        for case in coord[2]:
            g = evaluation(N, game, coord, color, case, False)
            if g == maxi:
                maximums.append(case)
        x, y = -1, -1
        for case in maximums:
            if case[0] == case[1] or case[0] == N - 1 - case[1]:
                x, y = case
        if x < 0:
            x, y = maximums[0]
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
