#coding:utf-8

import config
from tkinter import messagebox
import socket

def JoinGame():
    recupConfig = config.learnConfig()
    try:
        host, port = (recupConfig["ipConnect"].strip(),int(recupConfig["port"].strip()))
        print((host,port))
        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serv.connect((host, port))
    except:
        print("y a un truc qui va pas :(")
    else:
        print("client connecté !")
        messagebox.showinfo("CLIENT","CONNECTION REUSSITE !")
        serv.sendall(recupConfig["pseudo"])

    

