#coding:utf-8

import tkinter
from tkinter import messagebox

def learnConfig():
    dicoConfig = {}
    with open("config.txt","r") as config:
        tableauConfig = config.readlines()
        for lines in tableauConfig:
            try:
                linesSplit = lines.split(":")
                dicoConfig[linesSplit[0]] = linesSplit[1]
            except:
                messagebox.showerror("ERREUR","un probleme dans la configuration est survenu !")
                break
    return dicoConfig

def menueConfig(window):
    dicoConfig = learnConfig()
    configMenue = tkinter.Toplevel(window)
    configMenue.title("")
    configMenue.geometry("300x200")
    configMenue.resizable(width=False,height=False)


    var_port = tkinter.StringVar()
    var_port.set(dicoConfig["port"])
    var_username = tkinter.StringVar()
    var_username.set(dicoConfig["username"])

    tkLabelPort = tkinter.Label(configMenue,text="port de connexion :")
    tkInputPort = tkinter.Entry(configMenue,textvariable=var_port)
    btChangePort = tkinter.Button(configMenue,text="changer")
    tkLabelPort.place(x=10,y=5)
    tkInputPort.place(x=120,y=5,width=50)
    btChangePort.place(x=175,y=4)

    tkLabelUsername = tkinter.Label(configMenue,text="Votre pseudo :")
    tkInputUsername = tkinter.Entry(configMenue,textvariable=var_username)
    btChangeUsername = tkinter.Button(configMenue,text="changer")
    tkLabelUsername.place(x=10,y=50)
    tkInputUsername.place(x=100,y=50,width=70)
    btChangeUsername.place(x=175,y=49)
    
    
    

if __name__ == "__main__":
    print(learnConfig())
    test = learnConfig()

    print(test["port"])