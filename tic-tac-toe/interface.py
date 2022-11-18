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
import tkinter as tk
import copy
import random
from tic_tac_toe_playable_tk import Game
from tkinter.messagebox import showinfo


class Interface(tk.Tk):
    def __init__(self, N):
        tk.Tk.__init__(self)
        self.frameCan = tk.Frame(self)
        self.frameCan.pack(side="top")
        self.N = N
        width, height = 600, 480
        self.canvas = tk.Canvas(self.frameCan, width=600, height=480, bg="white")
        self.canvas.bind(
            "<Button-1>", self.onClick_souris
        )  # <Button-1> : Bouton gauche de la souris
        self.canvas.pack()
        for i in range(1, N):
            self.canvas.create_line(int(width * i / N), 0, int(width * i / N), 479)
            self.canvas.create_line(0, int(height * i / N), 599, int(height * i / N))
        self.game = Game(N, self)
        self.morpion = Morpion(self)
        self.frameButton = tk.Frame(self)
        self.frameButton.pack(side="bottom")
        self.listButton = []
        button1 = tk.Button(self.frameButton, text="Recommencer", command=self.reset)
        button1.pack()
        self.listButton.append(button1)
        button2 = tk.Button(
            self.frameButton, text="Changer la taille", command=self.change_N
        )
        button2.pack()
        self.listButton.append(button2)
        self.humain = False
        self.len = N
        self.liste_cases = []
        self.liste_cases_opposee = []
        # Création de la liste des cases pour y tracer les formes
        for j in range(N):
            for i in range(N):
                self.liste_cases.append(
                    [
                        int(width * i / N) + 1,
                        int(height * j / N) + 1,
                        int(width * i / N) + int(width / N) - 1,
                        int(height * j / N) - 1 + int(height / N),
                    ]
                )
                # Permet de tracer les croix facilement
                self.liste_cases_opposee.append(
                    [
                        int(width * i / N) + 1,
                        int(height * j / N) - 1 + int(height / N),
                        int(width * i / N) + int(width / N) - 1,
                        int(height * j / N) + 1,
                    ]
                )

    def change_N(self):
        self.N = 3 if self.N == 5 else 5
        width, height = 600, 480
        self.canvas.pack_forget()
        self.canvas = tk.Canvas(self.frameCan, width=600, height=480, bg="white")
        self.canvas.bind(
            "<Button-1>", self.onClick_souris
        )  # <Button-1> : Bouton gauche de la souris
        self.canvas.pack()
        for i in range(1, self.N):
            self.canvas.create_line(
                int(width * i / self.N), 0, int(width * i / self.N), 479
            )
            self.canvas.create_line(
                0, int(height * i / self.N), 599, int(height * i / self.N)
            )
            self.liste_cases = []
        self.liste_cases_opposee = []
        # Création de la liste des cases pour y tracer les formes
        N = self.N
        for j in range(N):
            for i in range(N):
                self.liste_cases.append(
                    [
                        int(width * i / N) + 1,
                        int(height * j / N) + 1,
                        int(width * i / N) + int(width / N) - 1,
                        int(height * j / N) - 1 + int(height / N),
                    ]
                )
                # Permet de tracer les croix facilement
                self.liste_cases_opposee.append(
                    [
                        int(width * i / N) + 1,
                        int(height * j / N) - 1 + int(height / N),
                        int(width * i / N) + int(width / N) - 1,
                        int(height * j / N) + 1,
                    ]
                )
        self.reset()

    def fonction1(self):
        print("On est dans fonction1; décider quoi faire si on clique sur Bouton 1")

    def fonction2(self):
        print("On est dans fonction2; décider quoi faire si on clique sur Bouton 2")

    def tracer(self, color, case):
        # Trace la forme dans la case, rond ou croix
        if not color:
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
        print(f"On a cliqué dans la case {(x,y)}")
        # Sur quelle case a-t-on cliqué ?
        for case in self.liste_cases:
            if x > case[0] and x < case[2] and y > case[1] and y < case[3]:
                index = self.liste_cases.index(case)
                self.morpion.place_pawn(index // self.N, index % self.N)

    def reset(self):
        self.game = Game(self.N, self)
        self.morpion = Morpion(self)
        self.morpion.repaint()


class Morpion:
    def __init__(self, interface):
        self.interface = interface
        self.N = self.interface.N
        self.matrice = self.interface.game.matrix
        self.player = False
        self.nombre_tour = 0
        self.case_a_vider = -1
        self.vainqueur = None

    def place_pawn(self, x, y):
        if (
            self.matrice[x][y] == float("inf")
            and len(self.interface.game.coord[self.player]) < self.N
        ):
            self.matrice[x][y] = self.player
            self.interface.game.coord[self.player].append((x, y))
            self.interface.game.coord[2].remove((x, y))

            self.interface.game.place_random(not self.player)

            self.repaint()

            if self.interface.game.ended(self.player):
                showinfo("Fin de partie", "Partie terminée : les ronds ont gagné !")
                self.interface.reset()

            elif self.interface.game.ended(not self.player):
                showinfo("Fin de partie", "Partie terminée : les croix ont gagné !")

        elif (
            self.matrice[x][y] == self.player
            and len(self.interface.game.coord[self.player]) == self.N
        ):
            self.case_a_vider = (x, y)
            self.matrice[x][y] = float("inf")
            self.interface.game.coord[self.player].remove((x, y))
            self.interface.game.coord[2].append((x, y))
            self.repaint()

    def repaint(self):
        for i in range(self.N):
            for j in range(self.N):
                self.interface.effacer(i * self.N + j)
                if self.matrice[i][j] == True:
                    self.interface.tracer(True, i * self.N + j)
                elif self.matrice[i][j] == False:
                    self.interface.tracer(False, i * self.N + j)


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
