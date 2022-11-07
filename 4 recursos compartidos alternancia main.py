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
            #Verifica si las conexiones entrantes tienen los tokens necesarios
            semaphore.acquire()
            if all(element.condition() for element in self.conexionesEntrada):
                print(f"Se ejecuta: {self.name}")
                #Le quita a los elementos entrantes los tokens
                for element in self.conexionesEntrada:
                    # print(f"tokens en {element.place.name} ANTES del disparo {element.place.tokens}"),
                    element.place.removeToken(element.weight)
                    # print(f"tokens en {element.place.name} DESPUES del disparo {element.place.tokens}"),
                #Le da a los elementos salientes sus tokens
                for element in self.conexionesSalida:
                    # print(f"tokens en {element.place.name} ANTES del disparo {element.place.tokens}"),
                    element.place.getToken(element.weight)
                    # print(f"tokens en {element.place.name} DESPUES del disparo {element.place.tokens}")
            else:
                print(f"No se pudo ejecutar {self.name}")
            print(f"M: ({p1.tokens}, {p2.tokens}, {p3.tokens}, {p4.tokens}, {p5.tokens}, {p6.tokens}, {p7.tokens}, {p8.tokens})")
            semaphore.release()


# Places de la red
p1 = Place(1, 'P1')
p2 = Place(0, 'P2')
p3 = Place(0, 'P3')
p4 = Place(1, 'P4')
p5 = Place(1, 'P5')
p6 = Place(0, 'P6')
p7 = Place(0, 'P7')
p8 = Place(0, 'P8')

print(f"M: ({p1.tokens}, {p2.tokens}, {p3.tokens}, {p4.tokens}, {p5.tokens}, {p6.tokens}, {p7.tokens}, {p8.tokens})")

# Conexiones de la red
connection1 = Connection(p1, 1)
connection2 = Connection(p2, 1)
connection3 = Connection(p2, 1)
connection4 = Connection(p3, 1)
connection5 = Connection(p3, 1)
connection6 = Connection(p1, 1)
connection7 = Connection(p4, 1)
connection8 = Connection(p8, 1)
connection9 = Connection(p4, 1)
connection10 = Connection(p8, 1)
connection11 = Connection(p5, 1)
connection12 = Connection(p6, 1)
connection13 = Connection(p6, 1)
connection14 = Connection(p7, 1)
connection15 = Connection(p7, 1)
connection16 = Connection(p5, 1)

# Transiciones de la red
t1 = Transition([connection1], [connection2], 't1')
t2 = Transition([connection3, connection10], [connection4], 't2')
t3 = Transition([connection5], [connection6, connection7], 't3')
t4 = Transition([connection11], [connection12], 't4')
t5 = Transition([connection13, connection9], [connection14], 't5')
t6 = Transition([connection15], [connection8, connection16], 't6')


# inicio los threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

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



