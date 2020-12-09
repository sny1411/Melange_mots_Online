#coding:utf-8

import socket
import tkinter
from tkinter.constants import END
import config
from tkinter import messagebox
import threading

GamePasDemarer = True
dicoConn = []

class wSalleAttente(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.wSalleAttente = None
        self.tkListeJoueur = None
    def run(self):
        self.wSalleAttente = tkinter.Tk()
        self.tkListeJoueur = tkinter.Listbox(self.wSalleAttente)
        self.wSalleAttente.title("Salle d'attente")
        self.tkListeJoueur.pack()
        wSalleAttente_x = 500
        wSalleAttente_y = 500
        self.wSalleAttente.geometry(f"{wSalleAttente_x}x{wSalleAttente_y}")
        self.wSalleAttente.resizable(width=False,height=False)
        self.wSalleAttente.mainloop()
    def newPlayer(self,pseudo):
        self.tkListeJoueur.insert("end", pseudo)
    def getTkList(self):
        return self.tkListeJoueur.get('@1,0',END)
    def removePlayerInList(self,i):
        self.tkListeJoueur.delete(i)

def attendreConnexion(serv,windowAttente,nbreClient):
    while GamePasDemarer:
        print("Je cherche des gens la")
        serv.listen(10)
        conn ,adress= serv.accept() # renvoie un tuple (conn et adress) mais pas besoin de adress la :)
        pseudoJoueur = conn.recv(16)
        pseudoJoueur = pseudoJoueur.decode("utf8")
        windowAttente.newPlayer(pseudoJoueur)
        dicoConn.append(conn)

        my_thread = ThreadForClient(conn,pseudoJoueur,windowAttente,nbreClient)
        my_thread.start()
        
        print("client connecté")

def runServeur():
    host, port = (None,None)
    serv = None
    try:
        recupConfig = config.learnConfig()
        host, port = ('', int(recupConfig["port"].strip()))
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serv.bind((host, port))
    except ValueError:
        messagebox.showerror("ERREUR","Le port n'est surement pas lisible")
    print(f"Le serveur est démarré sur le port {port}")
    nbreClient = NbreClientsCo()
    windowAttente = wSalleAttente()
    windowAttente.start()
    attCO = threading.Thread(target= lambda : attendreConnexion(serv,windowAttente,nbreClient))
    attCO.start()
    
    
class NbreClientsCo():
    def __init__(self):
        self.nbreClient = 0

    def newPlayer(self):
        self.nbreClient += 1
    
    def decoClient(self):
        self.nbreClient -= 1
    
    def getNbreClient(self):
        return self.nbreClient
    

class ThreadForClient(threading.Thread):
    def __init__(self, conn,pseudoJoueur,windowAttente,nbreClient):
        threading.Thread.__init__(self)
        self.conn = conn
        self.pseudo = pseudoJoueur
        self.windowAttente = windowAttente
        self.nbreClient = nbreClient

    def run(self):
        print(self.conn)
        while True:
            data = self.conn.recv(1024)
            print(dicoConn[:])
            for msg in dicoConn:
                msg.sendall(data)
            data = data.decode("utf8")
            if not data: break
        self.conn.close()
        dicoConn.remove(self.conn)
        print("client deconnecter")
        listPseudo = self.windowAttente.getTkList()
        print(listPseudo)
        i = 0
        for pseudo in listPseudo:
            print(pseudo)
            if pseudo == self.pseudo:
                self.windowAttente.removePlayerInList(i)
                i += 1
                break
            print(data)

def game():
    wGameHost = tkinter.Tk()
    wGameHost.title("Mélange mots - HOST")
    wGameHost_x = 600
    wGameHost_y = 500
    wGameHost.geometry(f"{wGameHost_x}x{wGameHost_y}")
    wGameHost.resizable(width=False,height=False)

