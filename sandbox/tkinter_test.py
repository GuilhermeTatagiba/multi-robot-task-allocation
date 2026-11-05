#Test_Tkinter

import tkinter as tk
from tkinter import *
import pandas as pd

from tkinter import Tk, Canvas, Button, LEFT, BOTTOM
from random import choice

# Exemple 1

class FooGUI:
    """FooGUI is a simple GUI for drawing some colorful lines."""
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, bg='dark grey', height=200, width=200)
        self.canvas.pack(side=LEFT)
        self.quit_but = Button(self.root, text='Quitter',
        command=self.root.destroy)

        self.quit_but.pack(side=BOTTOM)
        self.draw_but = Button(self.root, text='Tracer une ligne',

        command=self.drawline)

        self.draw_but.pack()
        self.col_but = Button(self.root, text='Autre couleur',
        command=self.changecolor)

        self.col_but.pack()
        self.coords = [10, 190, 190, 10]
        self.palette = ['purple', 'cyan', 'maroon', 'green',
        'red', 'blue', 'orange', 'yellow']

        self.color = choice(self.palette)
        self.root.mainloop()
    def drawline(self):
        """Draw a line in the Canvas and shift next line's coordinates."""
        self.canvas.create_line(*self.coords, width=2, fill=self.color)
        self.coords[1] -= 10
        self.coords[3] += 10
    def changecolor(self):
        """Random change of the next lines' color."""
        self.color = choice(self.palette)

# Exemple 2
        
class RoomGUI:
    '''RoomGUI est une classe qui permet de tracer une pièce en utilisant la bibliothèque tkinter'''

    def __init__(self, largeur=200, longueur=200, liste_murs=[]):
        self.root = Tk()

        #création d'un canvas pour dessiner
        self.canvas = Canvas(self.root, bg='white', height=200, width=200)
        self.canvas.pack(side=LEFT)

        #ajout d'un bouton pour quitter l'application
        self.quit_but = Button(self.root, text='Quitter', command=self.root.destroy, bg='red')
        self.quit_but.pack(side=BOTTOM)



        self.coords = [10, 190, 190, 10] 
        self.palette = ['purple', 'cyan', 'maroon', 'green', 'red', 'blue', 'orange', 'yellow']
        self.root.mainloop()

        #ajout des murs
        self.liste_murs = liste_murs
        liste_mur_ext = [[[0,0], [0, largeur]], [[0, largeur], [longueur, largeur]], 
            [[longueur, largeur], [longueur, 0]], [[longueur, 0], [0, 0]]]
        self.liste_murs += liste_mur_ext
        for mur in liste_murs:
            self.dessine_mur(mur, 'black')
            
    def dessine_mur(self, coords, couleur='black'):
        '''
        Trace une ligne dans le canvas
        Les coordonnées sont données sous forme de liste de deux listes de deux éléments
        Par exemple [[10, 10], [10, 190]] pour un mur vertical
            
        '''
        self.canvas.create_line(coords, width=2, fill=couleur)


# Lis le fichier txt
df_murs = pd.read_excel('Programmes_2024\murs_techlab.xlsx', header=0)


# On créer une liste de murs
liste_murs = []
for i in range(len(df_murs)):
    position = [[df_murs.iloc[i, 0], df_murs.iloc[i, 1]], [df_murs.iloc[i, 2], df_murs.iloc[i, 3]]]
    liste_murs.append(position)

# Test de la classe RoomGUI
RoomGUI(liste_murs=liste_murs)