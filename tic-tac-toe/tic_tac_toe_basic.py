# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:15:16 2022

@author: AS
"""
import random
def play(Game, N, coord):
    color = False
    end = False
    while not end:
        place(Game, N, color, coord)
        end = win(Game, N, color)
        if not end:
            color= not color
    return color



def place(Game, N, color, coord):
    i,j=-1,-1
    if len(coord[color])==N:
        rd=random.randint(0,N-1)
        i,j=coord[color][rd]
    found=False
    while not found:
        x,y = random.randint(0,N-1),random.randint(0,N-1)
        print(x,y)
        print(coord)
        print(Game)
        if Game[x][y]==float("inf"):
            Game[x][y]=color
            coord[color].append((x,y))
            coord[2].remove((x,y))
            if i>=0:
                coord[color].remove((i,j))
                coord[2].append((i,j))
                Game[i][j]=float("inf")
            found=True
            print('trouve')




def win(Game, N, color):
    for i in range(len(Game)):
        S=sum(Game[i])
        if S==N*color:
            return True
        S=sum([Game[k][i] for k in range(N)])
        if S==N*color:
            return True
    S=sum([Game[i][i] for i in range(N)])
    if S==N*color:
        return True
    S=sum([Game[i][N-i-1] for i in range(N)])
    if S==N*color:
        return True
    return False



def initialize(N):
    Game = [[float("inf") for i in range(N)] for j in range(N)]
    coord=[[],[],[]]
    for i in range(N):
        for j in range(N):
            coord[2].append((i,j))
    print('Noirs' if play(Game, N, coord) else 'Blancs')
    
if __name__=='__main__':
    initialize(3)