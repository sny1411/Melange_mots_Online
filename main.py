#coding:utf-8

import tkinter
import socket

def clickOnHost():
    pass

def clickOnJoin():
    pass

window = tkinter.Tk()
window.title("Mélange mots - ONLINE")
window_x = 350
window_y = 150
window.geometry(f"{window_x}x{window_y}")
window.resizable(width=False,height=False)

tkBtnHost = tkinter.Button(window, text="Héberger une partie",command=clickOnHost)
tkBtnJoin = tkinter.Button(window, text="Rejoindre une partie",command=clickOnJoin)

tkBtnHost.place(x=window_x//2 - 75,y=10, width=150,height=50)
tkBtnJoin.place(x=window_x//2 - 75,y=70, width=150,height=50)

window.mainloop()
