
import threading
import time

from Place import Place

class Transition(threading.Thread):

    conexionesSalida:Place
    conexionesEntrada:Place

    def __init__(self, conexionesEntrada, conexionesSalida):
        threading.Thread.__init__(self)
        self.conexionesEntrada = conexionesEntrada
        self.conexionesSalida = conexionesSalida

    def run(self):
        self.conexionesSalida.getToken(1)