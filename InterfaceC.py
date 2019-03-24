# coding: utf-8

import socket
from threading import Thread
import sys
from tkinter import *
from functools import *
from Client import *
def interface():
	fenetre = Tk()

	fenetre.title('Chat en ligne')
	fenetre.geometry("1000x600")
	fenetre.resizable(0, 0)

	def Entrepseudo():
		#ON SE CONNECTE AU SERVEUR AVEC LE PSEUDO ET ON DETRUIT LES WIDGETS POUR EN METTRE DE NOUVEAU
		ConnexionAuServeur(EntreePseudo.get())
		Button_connexion.destroy()
		EntreePseudo.destroy()

	#ON DEFINI ET AFFICHE LE BOUTON ET LE CHAMP DE SAISIE
	EntreePseudo = Entry(fenetre, width=30)
	EntreePseudo.pack()
	Button_connexion = Button(fenetre, text="Connexion au serveur", command=partial(Entrepseudo))
	Button_connexion.pack()


	fenetre.mainloop()

if __name__ == '__main__':
    interface()
