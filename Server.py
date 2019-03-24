# coding: utf-8

import socket
from threading import Thread
import sys
host="127.0.0.1"
port = 15555


class Serveurclient(Thread):
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion

    def run(self):
        nom = self.getName()
        while True:
            try :
                message_recu = self.connexion.recv(1024).decode("Utf8")
                if message_recu == "FIN":
                    break
                message = "%s > %s" % (nom, message_recu)
                print(message)
                for cle in conn_client:
                    if cle != nom:
                        conn_client[cle].send(message.encode("Utf8"))
            except :
                del conn_client[nom]
        self.connexion.close()
        del conn_client[nom]
        print("Client %s déconnecté" % nom)



#INITIALISE LE SERVEUR ET ATTEND UNE CONNEXION ENTRANTE
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  mySocket.bind((host, port))
except socket.error:
  print("La liaison du socket à l'adresse choisie a échoué.")
  sys.exit()
print("Serveur prêt, en attente de requêtes ...")
mySocket.listen(5)

conn_client = {}
while 1:
    connexion, adresse = mySocket.accept()
    th = Serveurclient(connexion)
    th.start()
    it = th.getName()
    conn_client[it] = connexion
    nom_client = []
    print("Client %s connecté, adresse IP %s, port %s" % (it, adresse[0], adresse[1]))

    msg="Vous etes connecté. Entrez votre pseudo \n"
    connexion.send(msg.encode("Utf8"))
