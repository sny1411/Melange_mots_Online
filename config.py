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

    var_port = tkinter.StringVar()
    var_port.set(dicoConfig["port"])
    var_username = tkinter.StringVar()
    var_username.set(dicoConfig["username"])

    tkLabelPort = tkinter.Label(configMenue,text="port de connexion :")
    tkInputPort = tkinter.Entry(configMenue,textvariable=var_port)
    tkLabelPort.pack()
    tkInputPort.pack()
    
    
    

if __name__ == "__main__":
    print(learnConfig())
    test = learnConfig()

    print(test["port"])