#POUVOIR RECEVOIR LES MSG EN DIRECT 
import socket
from threading import Thread
import sys
from InterfaceC import *
host="127.0.0.1"
port = 15555
#ON RAJOUTE LA VAR GLOBALE POUR FAIRE UNE BOUCLE ET RECUPERER LE PSEUDO
global connaitre_pseudo 
connaitre_pseudo = True
class ClientRecevoir(Thread):
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion

    def run(self):
        while 1:
            response = self.connexion.recv(1024).decode("Utf8")
            print(response)
        
class ClientEnvoi(Thread):
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion

    def run(self):
	#ICI LA BOUCLE
        while connaitre_pseudo:
            message_envoi = pseudo1
            self.connexion.send(message_envoi.encode("Utf8"))
            connaitre_pseudo = False
        while 1:
            message_envoi = input("")
            if message_envoi == "FIN":
                self.connexion.send(message_envoi.encode("Utf8"))
                print("Client arrêté. Connexion interrompue.")
                self.connexion.close()
                sys.exit(0)
            self.connexion.send(message_envoi.encode("Utf8"))

def ConnexionAuServeur(pseudo):
	global pseudo1
	pseudo1 = pseudo
	print("hey")
	connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	  connexion.connect((host, port))
	except socket.error:
	  print("La connexion a échoué.")
	  sys.exit()
	print("Connexion établie avec le serveur.")
	oui = ClientRecevoir(connexion)
	non = ClientEnvoi(connexion)
	oui.start()
	non.start()
	print("les threads sont lancés")

if __name__ == '__main__':
    ConnexionAuServeur()
