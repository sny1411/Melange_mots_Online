#coding:utf-8

import pickle
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


if __name__ == "__main__":
    print(learnConfig())