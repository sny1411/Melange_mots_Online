#coding:utf-8

import socket
import tkinter
import config
from tkinter import messagebox
import threading

GamePasDemarer = True
dicoConn = []

class wSalleAttente(threading.Thread):

    def __init__(self):
        wSalleAttente = tkinter.Tk()
        wSalleAttente.title("Salle d'attente")
        wSalleAttente_x = 500
        wSalleAttente_y = 500
        wSalleAttente.geometry(f"{wSalleAttente_x}x{wSalleAttente_y}")
        wSalleAttente.resizable(width=False,height=False)

        self.tkListeJoueur = tkinter.Listbox(wSalleAttente)
        self.tkListeJoueur.pack()
        
        wSalleAttente.mainloop()
    def newPlayer(self,pseudo):
        self.tkListeJoueur.insert("end", pseudo)
def attendreConnexion(serv,windowAttente):
    while GamePasDemarer:
        print("Je cherche des gens la")
        serv.listen(10)
        conn ,adress= serv.accept() # renvoie un tuple (conn et adress) mais pas besoin de adress la :)
        pseudoJoueur = conn.recv(16)
        pseudoJoueur = pseudoJoueur.decode("utf8")
        windowAttente.newPlayer(pseudoJoueur)
        dicoConn.append(conn)

        my_thread = ThreadForClient(conn,pseudoJoueur)
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

    windowAttente = wSalleAttente()
    attCO = threading.Thread(target= lambda : attendreConnexion(serv,windowAttente))
    attCO.join()
    windowAttente.join()
    attCO.start()
    windowAttente.start()
    
    
    

class ThreadForClient(threading.Thread):
    def __init__(self, conn,pseudoJoueur):
        threading.Thread.__init__(self)
        self.conn = conn
        self.pseudo = pseudoJoueur

    def run(self):
        print(self.conn)
        while True:
            data = self.conn.recv(1024)
            print(dicoConn[:])
            for msg in dicoConn:
                msg.sendall(data)
            data = data.decode("utf8")
            if not data:
                dicoConn.remove(self.conn)
                print("client deconnecter")
                self.conn.close()
                break

            print(data)
            if data == "deco()":
                print("client deconnecter")
                self.conn.close()
                break


def game():
    wGameHost = tkinter.Tk()
    wGameHost.title("Mélange mots - HOST")
    wGameHost_x = 600
    wGameHost_y = 500
    wGameHost.geometry(f"{wGameHost_x}x{wGameHost_y}")
    wGameHost.resizable(width=False,height=False)

