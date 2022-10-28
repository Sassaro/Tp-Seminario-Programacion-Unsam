from ast import arg
import threading
import time
from tkinter import Y

#Place hereda de Thread
class Place(threading.Thread):

    def __init__(self, conexionesEntrada, conexionesSalida, tokens):
        threading.Thread.__init__(self)
        #Transiciones a las que esta conectado este place entrantes
        self.conexionesEntrada = conexionesEntrada
        #Transiciones a las que esta conectado este place saliente
        self.conexionesSalida = conexionesSalida
        #Tokens contenidos en el place
        self.tokens = tokens

#Esta funcion overridea la funcion run de thread
    def run(self):
        print(self.tokens)

    def getToken(self,tokens:int):
        self.tokens += tokens



if __name__ == "__main__":
    hola = Place(1,1,1)