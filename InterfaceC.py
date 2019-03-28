# coding: utf-8

import socket
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
                boul = 1
                print("thread lancé")
                texte = StringVar()
                message_tempo = ""
                Affichage = Label(fenetre, textvariable=texte)
                while boul:
                    try:
                        message_recu = recevoirClient()
                        if message_recu != message_tempo:
                            texte.set(message_recu)
                            Affichage.configure(textvariable=texte)
                            Affichage.pack()
                            message_tempo = message_recu
                    except :
                        print("impossible de trouver le texte")
                        break

        #SE LIE A LA FONCTION EnvoiClient(message)
        def envoi(message):
            EnvoiClient(message.get())
                
        def Chat():
            global thread1
            EntreeMsg = Entry(fenetre, width=30)
            EntreeMsg.pack()
            Button_envoyer = Button(fenetre, text="Envoyer", command=partial(envoi,EntreeMsg))
            Button_envoyer.pack()
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
