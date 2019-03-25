#POUVOIR RECEVOIR LES MSG EN DIRECT 
import socket
from threading import Thread
import sys
host="127.0.0.1"
port = 15555
#ON RAJOUTE LA VAR GLOBALE POUR FAIRE UNE BOUCLE ET RECUPERER LE PSEUDO
global connaitre_pseudo
global message_tempo
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
        global connaitre_pseudo
	#ICI LA BOUCLE
        global message_envoi
        while connaitre_pseudo:
            message_envoi = pseudo1
            self.connexion.send(message_envoi.encode("Utf8"))
            connaitre_pseudo = False
        global message_tempo
        message_tempo = pseudo1
        while 1:
            #ON PEUT PAS REGARDER H24 message_envoi SINON CA VA SPAM LE MEME MESSAGE 
            #DONC ON VERIFIE SI message_envoi == message_tempo
            #SI C'EST LE CAS ON SKIP ET LA BOUCLE RECOMMENCE
            #SINON ON ENVOI LE MSG AU SERVEUR ET ON DIT A message_tempo D'ETRE EGALE A message_envoi
            #CE QUI RAMENE A LA CONDITION POUR PAS SPAMMER LE SERVEUR 
            if message_envoi != message_tempo:
                if message_envoi == "FIN":
                    self.connexion.send(message_envoi.encode("Utf8"))
                    print("Client arrêté. Connexion interrompue.")
                    self.connexion.close()
                    sys.exit(0)
                self.connexion.send(message_envoi.encode("Utf8"))
                message_tempo = message_envoi

                
#RECEPTIONNE LE MESSAGE ET LE STOCKE DANS LA VAR message_envoi
def EnvoiClient(message):
    global message_envoi
    message_envoi = message
    
def ConnexionAuServeur(pseudo):
	global pseudo1
	pseudo1 = pseudo
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
    InterfaceC.Chat()
