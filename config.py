#coding:utf-8

import os.path
import tkinter
from tkinter import messagebox


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
    var_ipConnect = tkinter.StringVar()
    var_ipConnect.set(dicoConfig["ipConnect"])

    tkLabelPort = tkinter.Label(configMenue,text="port de connexion :")
    tkInputPort = tkinter.Entry(configMenue,textvariable=var_port)
    tkLabelPort.place(x=10,y=5)
    tkInputPort.place(x=120,y=5,width=50)

    tkLabelUsername = tkinter.Label(configMenue,text="Votre pseudo :")
    tkInputUsername = tkinter.Entry(configMenue,textvariable=var_username)
    tkLabelUsername.place(x=10,y=50)
    tkInputUsername.place(x=100,y=50,width=70)

    tkLabelIpConnect = tkinter.Label(configMenue,text="ip de connection :")
    tkInputIpConnect = tkinter.Entry(configMenue,textvariable=var_ipConnect)
    tkLabelIpConnect.place(x=10,y=95)
    tkInputIpConnect.place(x=120,y=95,width=100)

    tkBtnSave = tkinter.Button(configMenue,text="Sauvegarder",command=lambda: saveSettings(var_port,var_username,var_ipConnect))
    tkBtnSave.place(x=75,y=175)
    tkBtnRetour = tkinter.Button(configMenue,text="Retour",command=configMenue.destroy)
    tkBtnRetour.place(x=150,y=175)

def learnConfig():
    dicoConfig = {}
    if os.path.exists("config.txt"):
        with open("config.txt","r") as config:
            tableauConfig = config.readlines()
            for lines in tableauConfig:
                try:
                    if lines.strip() == "":
                        print("line vide")
                    else:
                        linesSplit = lines.split(":")
                        dicoConfig[linesSplit[0]] = linesSplit[1]
                except:
                    messagebox.showerror("ERREUR","un probleme dans la configuration est survenu !")
                    break
    else:
        print("probleme de fichier")
    return dicoConfig

def saveSettings(var_port,var_username,var_ipConnect):
    with open("config.txt","w") as config:
        line = f"port:{var_port.get()}\nusername:{var_username.get()}\nipConnect:{var_ipConnect.get()}"
        config.write(line)


if __name__ == "__main__":
    print(learnConfig())
    test = learnConfig()
    print(test["port"])
