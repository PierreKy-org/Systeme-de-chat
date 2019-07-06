# coding: utf-8

import socket
import time
from threading import Thread
import sys
from tkinter import *
from functools import *
from Client import *
global msg
global boul
def interface():
        fenetre = Tk()
        fenetre.title('Chat en ligne')
        fenetre.geometry("1000x600")
        fenetre.resizable(0, 0)

        class InterfaceRecu(Thread):
            def __init__(self):
                Thread.__init__(self)

            def run(self):
                global boul
                Flux = Frame(fenetre, width = 800, height = 500, bg = "red")
                Flux.grid_propagate(0)
                Flux.grid(row = 0, column = 0)
                boul = 1
                texte = StringVar()
                message_tempo = ""
                ListeTest = []
                i = 0
                while boul:
                    try:
                        message_recu = recevoirClient()
                        if message_recu != message_tempo:
                            texte.set(message_recu)
                            ListeTest.append(Label(Flux, text=message_recu, bg = "blue"))
                            for j in ListeTest:
                                j.grid(row = i, column = 1)
                                i += 1
                            message_tempo = message_recu
                    except :
                        print("impossible de trouver le texte")
                        break
                    time.sleep(1)
                
        #SE LIE A LA FONCTION EnvoiClient(message)
        def envoi(message):
            EnvoiClient(message.get())

        def Chat():
            global thread1

            Envoi = Frame(fenetre,width = 270, height = 27, bg ="green")
            Envoi.grid_propagate(0)
            Envoi.grid(row=1, column = 0)

            EntreeMsg = Entry(Envoi, width=30)
            EntreeMsg.grid(row = 0, column = 0, padx = 10)
            Button_envoyer = Button(Envoi, text="Envoyer", command=partial(envoi,EntreeMsg))
            Button_envoyer.grid(row = 0, column = 1, padx = 10)
            thread1 = InterfaceRecu()
            thread1.start()
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
        boul = 0
        QuitClient()
if __name__ == '__main__':
        interface()
