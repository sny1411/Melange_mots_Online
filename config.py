#coding:utf-8

import pickle
def learnConfig():
    with open("config.txt","r") as config:
        print(config.readlines())


if __name__ == "__main__":
    learnConfig()