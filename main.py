#coding:utf-8

import tkinter
import socket

def clickOnHost():
    host, port = ('', 5566)
    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv.bind((host, port))
    print(f"Le serveur est démarré sur le port {port}")
    windowMenu.quit()
def clickOnJoin():
    windowMenu.quit()

windowMenu = tkinter.Tk()
windowMenu.title("Mélange mots - ONLINE")
windowMenu_x = 350
windowMenu_y = 150
windowMenu.geometry(f"{windowMenu_x}x{windowMenu_y}")
windowMenu.resizable(width=False,height=False)

tkBtnHost = tkinter.Button(windowMenu, text="Héberger une partie",command=clickOnHost)
tkBtnJoin = tkinter.Button(windowMenu, text="Rejoindre une partie",command=clickOnJoin)

tkBtnHost.place(x=windowMenu_x//2 - 75,y=10, width=150,height=50)
tkBtnJoin.place(x=windowMenu_x//2 - 75,y=70, width=150,height=50)

windowMenu.mainloop()
