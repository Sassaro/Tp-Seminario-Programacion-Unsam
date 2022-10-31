
from Connections import Connection
from Place import Place
from Transition import Transition


def main():

    maquinaExpendedora()


#Esta funcion crea una red de petri de una maquina expendedora (ejemplo del pdf)
def maquinaExpendedora():
    #Places de la red
    P0 = Place(1)
    P1 = Place(0)
    P2 = Place(0)
    P3 = Place(0)
    P4 = Place(0)
    #Conexiones de la red
    connection1 = Connection(P0,1)
    connection2 = Connection(P1,1)
    connection3 = Connection(P2,1)
    connection4 = Connection(P3,1)
    connection5 = Connection(P4,1)
    #Transiciones de la red
    dep5c = Transition([connection1],[connection2], "Se depositan 5 centavos 1")
    dep10c = Transition([connection1],[connection3], "Se depositan 10 centavos 2")
    dep5c2 = Transition([connection2],[connection3], "Se depositan 5 centavos 3")
    dep10c2 = Transition([connection2],[connection4],"Se depositan 10 centavos 4")
    dep5c3 = Transition([connection3],[connection4], "Se depositan 5 centavos 5")
    dep10c3 = Transition([connection3],[connection5], "Se depositan 10 centavos 6")
    dep5c4 = Transition([connection4],[connection5], "Se depositan 5 centavos 7")
    retira15 = Transition([connection4],[connection1],"Se compra por 15 8")
    retira20 = Transition([connection5],[connection1], "Se compra por 20 9")

    #Se inicializan los threads
    dep5c.start()
    dep10c.start()
    dep5c2.start()
    dep10c2.start()
    dep10c3.start()
    dep5c3.start()
    dep5c4.start()
    retira15.start()
    retira20.start()

    dep5c.join()
    dep10c.join()
    dep5c2.join()
    dep10c2.join()
    dep10c3.join()
    dep5c3.join()
    dep5c4.join()
    retira15.join()
    retira20.join()



if __name__ == "__main__":
    main()
