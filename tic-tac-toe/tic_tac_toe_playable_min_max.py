# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:30:25 2022

@author: AS
"""



def interest(N,game,coord,color,case):
    ncolor = not color
    player, opponent=0,0
    for i in range(N):
        NL1,NL2,NC1,NC2=0,0,0,0
        for j in range(N):
            if game[i][j]==color:
                NL1+=1
            if game[i][j]==ncolor:
                NL2+=1
            if game[j][i]==color:
               NC1+=1
            if game[j][i]==ncolor:
                NC2+=1
        if NL1==N or NC1==N:
            return float("inf")
        if NL2==N or NC2==N:
            return -float("inf")
        if NL1==0:
            opponent+=1
        if NL2==0:
            player+=1
        if NC2==0:
            player+=1
        if NL1==0:
            opponent+=1 
    return(player-opponent)


        
            
    return(player-opponent)
        

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
