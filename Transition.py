
import threading
import time
from tokenize import String
from Connections import Connection

from Place import Place

class Transition(threading.Thread):

    def __init__(self, conexionesEntrada:set[Connection], conexionesSalida:set[Connection], nombre:String):
        threading.Thread.__init__(self)
        self.conexionesEntrada = conexionesEntrada
        self.conexionesSalida = conexionesSalida
        self.nombre = nombre

    def run(self):
        
        aux = True

        while aux:
            time.sleep(1)
            #Verifica si las conexiones entrantes tienen los tokens necesarios
            if( all( element.condition() for element in self.conexionesEntrada ) ):
                aux = False
                print("Se ejecuta:", self.nombre)
                #Le quita a los elementos entrantes los tokens
                for element in self.conexionesEntrada:
                    element.place.removeToken(element.weight)
                #Le da a los elementos salientes sus tokens
                for element in self.conexionesSalida:
                    element.place.getToken(element.weight)
        
        