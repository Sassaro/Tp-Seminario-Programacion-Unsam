from multiprocessing import Semaphore
import threading
import time

semaphore = Semaphore(1)


class Place:
    def __init__(self, tokens, name: str):
        self.tokens = tokens
        self.name = name

    def getToken(self, tokens):
        self.tokens += tokens

    def removeToken(self, tokens):
        self.tokens -= tokens


class Connection:

     def __init__(self, place: Place, weight):
         self.place = place
         self.weight = weight

     def condition(self) -> bool:
        return self.place.tokens >= self.weight


class Transition(threading.Thread):

     def __init__(self, conexionesEntrada: Connection, conexionesSalida: Connection, name: str):
         threading.Thread.__init__(self)
         self.conexionesEntrada = set(conexionesEntrada)  # estas son las que deben cumplir la condicion
         self.conexionesSalida = set(conexionesSalida)
         self.name = name

     def run(self):

        aux = True
        while aux:
            #Duermo los threads para que se vayan cambiando de turno
            time.sleep(0.5)
            semaphore.acquire()
            # Verifica si las conexiones entrantes tienen los tokens necesarios
            if all(element.condition() for element in self.conexionesEntrada):
                print(f"Se ejecuta: {self.name}")
                #Le quita a los elementos entrantes los tokens
                for element in self.conexionesEntrada:
                    element.place.removeToken(element.weight)
                #Le agrega a los elementos salientes sus tokens
                for element in self.conexionesSalida:
                    element.place.getToken(element.weight)
            else:
                print(f"No se pudo ejecutar {self.name}")
            print(f"M: {p1.tokens, p2.tokens, p3.tokens,p4.tokens,p5.tokens}")
            semaphore.release()


# Places de la red
p1 = Place(1, 'P1')
p2 = Place(0, 'P2')
p3 = Place(0, 'P3')
p4 = Place(1, 'P4')
p5 = Place(0, 'P5')

print(f"M: {p1.tokens, p2.tokens, p3.tokens, p4.tokens, p5.tokens}")  # marca 0

# Conexiones de la red
connection1 = Connection(p1, 1)
connection2 = Connection(p2, 1)
connection3 = Connection(p2, 1)
connection4 = Connection(p1, 1)
connection5 = Connection(p3, 10)  # para que se vea con mas claridad
connection6 = Connection(p3, 10)  # para que se vea con mas claridad
connection7 = Connection(p4, 1)
connection8 = Connection(p5, 1)
connection9 = Connection(p5, 1)
connection10 = Connection(p4, 1)

# Transiciones de la red
t1 = Transition([connection1], [connection2], 't1')
t2 = Transition([connection3], [connection4, connection5], 't2')
t3 = Transition([connection6, connection7], [connection8], 't3')
t4 = Transition([connection9], [connection10], 't4')


# inicio los threads
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

# secuencias de disparos CUANDO no tengo threads
#
# s1 = (t1, t2, t1, t2, t1, t2)
# print(f"M0: {p1.tokens, p2.tokens, p3.tokens,p4.tokens}")
#
# for t in s1:
#     t.run()
#print(f"M1: {p1.tokens, p2.tokens, p3.tokens,p4.tokens}")
# t2.run()
#print(f"M2: {p1.tokens, p2.tokens, p3.tokens,p4.tokens}")


# print(connection1.place.name, connection1.place.tokens)
# print(t1.name, t1.conexionesEntrada, t1.conexionesSalida)
# print(t2.name, t2.conexionesEntrada, t2.conexionesSalida)



