
from multiprocessing import Semaphore
from multiprocessing.connection import wait
import random
import threading
import time
from tokenize import String
from Connections import Connection

from Place import Place

semaphore = Semaphore(1)
list1 = [0.5, 0.6, 0.7, 0.8, 0.9, 1]


class Transition(threading.Thread):

    def __init__(self, conexionesEntrada:set[Connection], conexionesSalida:set[Connection], nombre:String):
        threading.Thread.__init__(self)
        self.conexionesEntrada = conexionesEntrada
        self.conexionesSalida = conexionesSalida
        self.nombre = nombre

    def run(self):
        
        aux = True
        while aux:
            #Duermo los threads para que se vayan cambiando de turno
            time.sleep(0.5)
            #Verifica si las conexiones entrantes tienen los tokens necesarios
            semaphore.acquire()
            if( all( element.condition() for element in self.conexionesEntrada ) ):
                print("Se ejecuta:", self.nombre)
                #Le quita a los elementos entrantes los tokens
                for element in self.conexionesEntrada:
                    element.place.removeToken(element.weight)
                #Le da a los elementos salientes sus tokens
                for element in self.conexionesSalida:
                    element.place.getToken(element.weight)
            semaphore.release()