# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:19:40 2022

@author: AS
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:30:25 2022

@author: AS
"""



def interest(N,game,color):
    
    if win(N, game, color):
        return float("inf")
    if win(N, game, not color):
        return -float("inf")
    
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
                
        if NL1==0:
            opponent+=1
        if NL2==0:
            player+=1
        if NC2==0:
            player+=1
        if NC1==0:
            opponent+=1 
            
    ND11,ND12,ND21,ND22=0,0,0,0
    for i in range(N):
        if game[i][i]==color:
            ND11+=1
        if game[i][i]==ncolor:
            ND12+=1
        if game[N-1-i][i]==color:
            ND21+=1
        if game[N-1-i][i]==ncolor:
            ND22+=1
            
    if ND11==0:
        opponent+=1
    if ND12==0:
        player+=1
    if ND22==0:
        player+=1
    if ND21==0:
        opponent+=1 
    return(player-opponent)

def min_max(N,game,deep_org,deep,method,color):
    if game!=[[float("inf") for i in range(N)] for j in range(N)]:
        if deep==0 or win(N,game,not color):
            score=interest(N,game,not color)
            return game,score
    min_score,max_score=float("inf"),-float("inf")
    best_move=None
    list_next_games=[]
    Ncolor=sum([game[i].count(color) for i in range(N)])
    if Ncolor<N:
        list_next_games=next_game_less_3(N,game,color)
    else:
        list_next_games=next_game_more_3(N,game,color)
    score_max,score_min=-float("inf"),float("inf")
    
    for game_bis in list_next_games:
        score=interest(N, game_bis, color)
        if score>score_max:
            score_max=score
        elif score<score_min:
            score_min=score
    limit=(score_max+score_min)/2  
        
    for game_bis in list_next_games:   
        if method:
            if interest(N, game_bis, color)>=limit:
                game1,score=min_max(N, game_bis,deep_org, deep-1,not method, not color)
                if score>max_score:
                    best_score=score
                    best_game= game1
                    max_score = best_score
        if not method:
            if interest(N, game_bis, color)<=limit:
                game1,score=min_max(N, game_bis,deep_org, deep-1,not method, not color)
                if score<min_score:
                    best_score=score
                    best_game= game1
                    min_score = best_score
              
    if deep==deep_org:
        return best_game,best_score
    return game,best_score

def next_game_less_3(N,game,color):
    liste=[]
    for i in range(N):
        for j in range(N):  
            if game[i][j]==float("inf"):
                game_bis=[[element for element in line] for line in game]
                game_bis[i][j]=color
                liste.append(game_bis)
    return liste

def next_game_more_3(N,game,color):
    liste=[]
    for i in range(N):
        for j in range(N):  
            if game[i][j]==color:
                liste_bis=next_game_less_3(N,game,color)
                for game_bis in liste_bis:
                    game_bis[i][j]=float("inf")
                liste=liste+liste_bis
    return liste
    
def maj_coord(N,game):
    coord=[[],[],[]]
    for i in range(N):
        for j in range(N):
            if game[i][j]==float("inf"):
                coord[2].append((i,j))
            elif game[i][j]:
                coord[True].append((i,j))
            elif not game[i][j]:
                coord[False].append((i,j))
    return coord

def play(N, game, coord,deep, human):
    color = False
    end = False
    while not end:
        if color == human:
            place_human(N, game, coord, color)
        else:
            game,score=min_max(N, game, deep, deep, True, color)
            coord=maj_coord(N, game)
        end = win(N, game, color)
        if not end:
            color = not color
    return color




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


def initialize(N,deep):
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
        if play(N, game, coord, deep, human)
        else "\nLes Blancs ont gagné !\n"
    )



if __name__ == "__main__":
    initialize(int(input("N = ? ")),int(input("Profondeur = ? ")))
