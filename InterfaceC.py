# coding: utf-8

import socket
from threading import Thread
import sys
from tkinter import *
from functools import *
from Client import *
global msg
def interface():
        fenetre = Tk()
        fenetre.title('Chat en ligne')
        fenetre.geometry("1000x600")
        fenetre.resizable(0, 0)

        #SE LIE A LA FONCTION EnvoiClient(message)
        def envoi(message):
                EnvoiClient(message.get())
                
        def Chat():
                EntreeMsg = Entry(fenetre, width=30)
                EntreeMsg.pack()
                Button_envoyer = Button(fenetre, text="Envoyer", command=partial(envoi,EntreeMsg))
                Button_envoyer.pack()
                
        def Entrepseudo():
                #ON SE CONNECTE AU SERVEUR AVEC LE PSEUDO ET ON DETRUIT LES WIDGETS POUR EN METTRE DE NOUVEAU
                ConnexionAuServeur(EntreePseudo.get())
                Button_connexion.destroy()
                EntreePseudo.destroy()
                Chat()
        #ON DEFINI ET AFFICHE LE BOUTON ET LE CHAMP DE SAISIE
        EntreePseudo = Entry(fenetre, width=30)
        EntreePseudo.pack()
        Button_connexion = Button(fenetre, text="Connexion au serveur", command=partial(Entrepseudo))
        Button_connexion.pack()


        fenetre.mainloop()
        QuitClient()
if __name__ == '__main__':
        interface()
