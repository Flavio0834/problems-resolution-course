import random


class Game:
    def __init__(self, N, human):
        self.matrix = [[float("inf") for i in range(N)] for j in range(N)]
        self.coord = [[], [], []]
        self.N = N
        for i in range(N):
            for j in range(N):
                self.coord[2].append((i, j))
        self.human = human

    def play(self):
        self.color = False
        self.end = False
        if self.color == self.human:
            self.place_human()
        else:
            self.place_random()
        self.end = self.ended()
        if not self.end:
            self.color = not self.color
        return self.end, self.color

    def place_random(self, color):
        i, j = -1, -1
        if len(self.coord[color]) == self.N:
            rd = random.randint(0, self.N - 1)
            i, j = self.coord[color][rd]
        found = False
        while not found:
            x, y = random.randint(0, self.N - 1), random.randint(0, self.N - 1)
            if self.matrix[x][y] == float("inf"):
                found = True
        if i >= 0:
            self.coord[color].remove((i, j))
            self.coord[2].append((i, j))
            self.matrix[i][j] = float("inf")
            # self.interface.morpion.place_pawn(i * N + j)
        self.matrix[x][y] = color
        self.coord[color].append((x, y))
        self.coord[2].remove((x, y))
        # self.interface.morpion.place_pawn(x * N + y)

    def place_human(self, x, y, x1=-1, y1=-1):
        x, y = -1, -1
        if len(self.coord[self.color]) == self.N:
            print("Il va falloir déplacer un pion.")
            while not ((x, y) in self.coord[2]):
                x, y = map(
                    int, input("Coordonnées du nouveau pion au format x y : ").split()
                )
        else:
            while not ((x, y) in self.coord[2]):
                x, y = map(int, input("Coordonnées du pion au format x y : ").split())
        if len(self.coord[self.color]) == N:
            x1, y1 = -1, -1
            while not ((x1, y1) in self.coord[self.color]):
                x1, y1 = map(
                    int, input("Coordonnées du pion à retirer au format x y : ").split()
                )
            self.matrix[x1][y1] = float("inf")
            self.coord[self.color].remove((x1, y1))
            self.coord[2].append((x1, y1))
        self.matrix[x][y] = self.color
        self.coord[self.color].append((x, y))
        self.coord[2].remove((x, y))

    def ended(self, color):
        for i in range(len(self.matrix)):
            S = sum(self.matrix[i])
            if S == self.N * color:
                return True
            S = sum([self.matrix[k][i] for k in range(self.N)])
            if S == self.N * color:
                return True
        S = sum([self.matrix[i][i] for i in range(self.N)])
        if S == self.N * color:
            return True
        S = sum([self.matrix[i][self.N - i - 1] for i in range(self.N)])
        if S == self.N * color:
            return True
        return False


if __name__ == "__main__":
    N = int(input("N = ? "))
    human = -1
    while human not in [0, 1]:
        human = int(input("Blancs ou noirs ? (0 ou 1) "))
    jeu = Game(N, human, None)
