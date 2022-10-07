# -*- coding: utf-8 -*-
"""
Sept 2020 : code minimal Tkinter pour Morpion
Tiré de l aversion plus complète "Code-Eleve-OK-MorpionFinal.py" de AC-2019-20
"""

"""
Ce code affiche une matrice pour le jeu Morpion puis en cas de clic dans une case, place aléatoirement
un 'rond' ou une 'croix' dans la case cliquée.
Si la case cliquée n'est pas vide, on la vide !
Deux boutons sont crées (bouton1, bouton2) pour la démo.
Ce code est une aide de base pour réaliser le BE 'Morpion' avec TkInter.
"""
import random
import tkinter as tk
import time
import copy


class Interface(tk.Tk):
    def __init__(self,N):
        tk.Tk.__init__(self)
        self.frameCan = tk.Frame(self)
        self.frameCan.pack(side="top")
        self.N=N
        width,height=600,480
        self.canvas = tk.Canvas(self.frameCan, width=600, height=480, bg="white")
        self.canvas.bind(
            "<Button-1>", self.onClick_souris
        )  # <Button-1> : Bouton gauche de la souris
        self.canvas.pack()
        for i in range(1,N):
            self.canvas.create_line(int(width*i/N), 0, int(width*i/N), 479)
            self.canvas.create_line(0, int(height*i/N), 599, int(height*i/N))
        self.morpion = Morpion(self)
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(side="bottom")
        self.listButton = []
        button1 = tk.Button(self.frameButton, text="Bouton 1", command=self.fonction1)
        button1.pack()
        self.listButton.append(button1)
        button2 = tk.Button(self.frameButton, text="Bouton 2", command=self.fonction2)
        button2.pack()
        self.listButton.append(button2)
        self.humain = False
        self.len=N
        self.liste_cases = []
        self.liste_cases_opposee = []
        # Création de la liste des cases pour y tracer les formes
        for j in range(N):
            for i in range(N):
                self.liste_cases.append(
                    [int(width*i/N)+1, int(height*j/N)+1, int(width*i/N)+int(width/N)-1, int(height*j/N)-1+int(height/N)]
                )
                # Permet de tracer les croix facilement
                self.liste_cases_opposee.append(
                    [int(width*i/N)+1, int(height*j/N)-1+int(height/N), int(width*i/N)+int(width/N)-1, int(height*j/N)+1]
                )

    def fonction1(self):
        print("On est dans fonction1; décider quoi faire si on clique sur Bouton 1")

    def fonction2(self):
        print("On est dans fonction2; décider quoi faire si on clique sur Bouton 2")

    def tracer(self, color, case):
        # Trace la forme dans la case, rond ou croix
        if color:
            self.canvas.create_oval(*(self.liste_cases[case]))
        else:
            self.canvas.create_line(*(self.liste_cases[case]))
            self.canvas.create_line(*(self.liste_cases_opposee[case]))
        self.update()

    def effacer(self, case):
        # vide la case
        self.canvas.create_rectangle(
            *(self.liste_cases[case]), fill="white", outline="white"
        )

    def onClick_souris(self, event):
        x = event.x
        y = event.y
        print(
            f"On a cliqué dans la case {(x,y)}; on affiche un 'O' ou 'X' dans la case (si vide)"
        )
        # Sur quelle case a-t-on cliqué ?
        for case in self.liste_cases:
            if x > case[0] and x < case[2] and y > case[1] and y < case[3]:
                self.morpion.place_pawn(
                    self.liste_cases.index(case)
                )


class Morpion:
    def __init__(self, interface):
        self.interface = interface
        self.N=self.interface.N
        self.matrice = [None for i in range(self.N**2)]
        self.player = True
        self.nombre_tour = 0
        self.case_a_vider = -1
        self.vainqueur = None
        self.IA = None

    def place_pawn(self, case):
        if self.matrice[case] == None and self.matrice.count(self.player)<self.N:
            self.matrice[case] = self.player
            self.repaint()
            self.player = not self.player
        elif self.matrice[case] == self.player:
            print(f"La case {case} n'est pas vide !")
            self.case_a_vider = case
            self.matrice[self.case_a_vider] = None
            self.repaint()

    def repaint(self):
        for i in range(self.N**2):
            self.interface.effacer(i)
            if self.matrice[i]==True :
                self.interface.tracer(True, i)
            elif self.matrice[i] == False:
                self.interface.tracer(False, i)


def printMatrice(M):
    for i in range(len(M)):
        print(M[i])


def adversaire(joueur):
    if joueur == "croix":
        return "rond"
    return "croix"


def copyMatrice(M):
    L = copy.deepcopy(M)
    return L


if __name__ == "__main__":
    jeu = Interface(5)
    jeu.mainloop()
