#coding:utf-8

import socket
import tkinter
import config

config = config.learnConfig()

def runServeur():

    host, port = ('', int(config["port"].strip()))
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv.bind((host, port))
    print(f"Le serveur est démarré sur le port {port}")

def TksalleAttenteJeu():
    wSalleAttente = tkinter.Tk()
    wSalleAttente.title("Salle d'attente")
    wSalleAttente_x = 500
    wSalleAttente_y = 500
    wSalleAttente.geometry(f"{wSalleAttente_x}x{wSalleAttente_y}")
    wSalleAttente.resizable(width=False,height=False)

    tkListeJoueur = tkinter.Listbox(wSalleAttente)
    tkListeJoueur.pack()

    wSalleAttente.mainloop()

def game():
    wGameHost = tkinter.Tk()
    wGameHost.title("Mélange mots - HOST")
    wGameHost_x = 600
    wGameHost_y = 500
    wGameHost.geometry(f"{wGameHost_x}x{wGameHost_y}")
    wGameHost.resizable(width=False,height=False)

if __name__ == "__main__":
    TksalleAttenteJeu()