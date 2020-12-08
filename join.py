#coding:utf-8

import config
from tkinter import messagebox
import socket
import time

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
        messagebox.showinfo("CLIENT","CONNECTION REUSSITE !")
        while True:
            time.sleep(100000)
