#coding:utf-8

import socket

def runServeur():
    host, port = ('', 5566)
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv.bind((host, port))
    print(f"Le serveur est démarré sur le port {port}")