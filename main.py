#coding:utf-8

import tkinter
import host
import join
import config



def clickOnHost():
    windowMenu.quit()
    windowMenu.destroy()
    host.runServeur()

def clickOnJoin():
    
    windowMenu.destroy()
    join.JoinGame()
def clickOnConfig():
    config.menueConfig(windowMenu)

windowMenu = tkinter.Tk()
windowMenu.title("Mélange mots - ONLINE")
windowMenu_x = 350
windowMenu_y = 200
windowMenu.geometry(f"{windowMenu_x}x{windowMenu_y}")
windowMenu.resizable(width=False,height=False)

tkBtnHost = tkinter.Button(windowMenu, text="Héberger une partie",command=clickOnHost)
tkBtnJoin = tkinter.Button(windowMenu, text="Rejoindre une partie",command=clickOnJoin)
tkBtnConfig = tkinter.Button(windowMenu, text="Configuration",command=clickOnConfig)

tkBtnHost.place(x=windowMenu_x//2 - 75,y=10, width=150,height=50)
tkBtnJoin.place(x=windowMenu_x//2 - 75,y=70, width=150,height=50)
tkBtnConfig.place(x = windowMenu_x//2 - 75,y=130, width=150,height=50)

windowMenu.mainloop()
