#coding:utf-8

import time
import tkinter
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
    except Exception as identifier:
        print(identifier)
    else:
        print("client connecté !")
        serv.sendall(recupConfig["username"].encode())
        print("connexion reussite")
        """
        messagebox.showinfo("CLIENT","CONNECTION REUSSITE !")
        tk = tkinter.Tk()
        tk.mainloop()
        """
        while True:
            print("oui")
            time.sleep(5)