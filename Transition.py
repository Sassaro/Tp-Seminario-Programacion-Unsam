
from multiprocessing import Semaphore
import threading
import time
from tokenize import String
from Connections import Connection

from Place import Place

#Se crea semaforo para que las transiciones no generen problemas por falta de exclusion mutua
semaphore = Semaphore(1)

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
            
            semaphore.acquire()#equivalente a Wait()
            #Verifica si las conexiones entrantes tienen los tokens necesarios
            if( all( element.condition() for element in self.conexionesEntrada ) ):

                #Muesta el texto para que se pueda ver como se va ejecutando la red de petri
                print("Se ejecuta:", self.nombre)

                #Le quita a los elementos entrantes los tokens

                for element in self.conexionesEntrada:
                    element.place.removeToken(element.weight)

                #Le da a los elementos salientes sus tokens

                for element in self.conexionesSalida:
                    element.place.getToken(element.weight)

            semaphore.release()#equivalente a Signal()