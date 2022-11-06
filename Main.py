
from Connections import Connection
from Place import Place
from Transition import Transition


def main():

    filosofosComensales()


#Esta funcion crea una red de petri de una maquina expendedora. (ejemplo del pdf)
def maquinaExpendedora():
    #Places de la red.
    P0 = Place(1)
    P1 = Place(0)
    P2 = Place(0)
    P3 = Place(0)
    P4 = Place(0)
    #Conexiones de la red.
    connection1 = Connection(P0,1)
    connection2 = Connection(P1,1)
    connection3 = Connection(P2,1)
    connection4 = Connection(P3,1)
    connection5 = Connection(P4,1)
    #Transiciones de la red.
    dep5c = Transition([connection1],[connection2], "Se depositan 5 centavos 1")
    dep10c = Transition([connection1],[connection3], "Se depositan 10 centavos 2")
    dep5c2 = Transition([connection2],[connection3], "Se depositan 5 centavos 3")
    dep10c2 = Transition([connection2],[connection4],"Se depositan 10 centavos 4")
    dep5c3 = Transition([connection3],[connection4], "Se depositan 5 centavos 5")
    dep10c3 = Transition([connection3],[connection5], "Se depositan 10 centavos 6")
    dep5c4 = Transition([connection4],[connection5], "Se depositan 5 centavos 7")
    retira15 = Transition([connection4],[connection1],"Se compra por 15 8")
    retira20 = Transition([connection5],[connection1], "Se compra por 20 9")

    aux = [dep5c,dep10c,dep5c2,dep10c2,dep10c3,dep5c3,dep5c4,retira15,retira20]

    #Se inicializan los threads.
    for i in aux:
        i.start()

    for i in aux:
        i.join()

#Esta funcion crea una red de petri de filosofos Comensales.
def filosofosComensales():
    #Places que representan los Filosofos Pensando. (Esperando comer)
    Filosofo1Pensando = Place(1)
    Filosofo2Pensando = Place(1)
    Filosofo3Pensando = Place(1)
    Filosofo4Pensando = Place(1)
    Filosofo5Pensando = Place(1)
    #Places que representan los tenedores en la mesa.
    Tenedor1 = Place(1)
    Tenedor2 = Place(1)
    Tenedor3 = Place(1)
    Tenedor4 = Place(1)
    Tenedor5 = Place(1)
    #Places que representan los filosofos cuando estan comiendo.
    Filosofo1Comiendo = Place(0)
    Filosofo2Comiendo = Place(0)
    Filosofo3Comiendo = Place(0)
    Filosofo4Comiendo = Place(0)
    Filosofo5Comiendo = Place(0)
    #Conexiones
    ConexionTenedor1 = Connection(Tenedor1,1)
    ConexionTenedor2 = Connection(Tenedor2,1)
    ConexionTenedor3 = Connection(Tenedor3,1)
    ConexionTenedor4 = Connection(Tenedor4,1)
    ConexionTenedor5 = Connection(Tenedor5,1)

    ConexionFilosofoPensando1 = Connection(Filosofo1Pensando,1)
    ConexionFilosofoPensando2 = Connection(Filosofo2Pensando,1)
    ConexionFilosofoPensando3 = Connection(Filosofo3Pensando,1)
    ConexionFilosofoPensando4 = Connection(Filosofo4Pensando,1)
    ConexionFilosofoPensando5 = Connection(Filosofo5Pensando,1)

    ConexionFilosofoComiendo1 = Connection(Filosofo1Comiendo,1)
    ConexionFilosofoComiendo2 = Connection(Filosofo2Comiendo,1)
    ConexionFilosofoComiendo3 = Connection(Filosofo3Comiendo,1)
    ConexionFilosofoComiendo4 = Connection(Filosofo4Comiendo,1)
    ConexionFilosofoComiendo5 = Connection(Filosofo5Comiendo,1)
    #Transiciones cuando los filosofos empiezan a comer.
    T_Filosofo1Come = Transition([ConexionFilosofoPensando1,ConexionTenedor1,ConexionTenedor2],[ConexionFilosofoComiendo1],"Filosofo 1 empieza a comer")
    T_Filosofo2Come = Transition([ConexionFilosofoPensando2,ConexionTenedor2,ConexionTenedor3],[ConexionFilosofoComiendo2],"Filosofo 2 empieza a comer")
    T_Filosofo3Come = Transition([ConexionFilosofoPensando3,ConexionTenedor3,ConexionTenedor4],[ConexionFilosofoComiendo3],"Filosofo 3 empieza a comer")
    T_Filosofo4Come = Transition([ConexionFilosofoPensando4,ConexionTenedor4,ConexionTenedor5],[ConexionFilosofoComiendo4],"Filosofo 4 empieza a comer")
    T_Filosofo5Come = Transition([ConexionFilosofoPensando5,ConexionTenedor5,ConexionTenedor1],[ConexionFilosofoComiendo5],"Filosofo 5 empieza a comer")
    #Transiciones cuando los filosofos dejan de comer.
    T_Filosofo1DejaDeComer = Transition([ConexionFilosofoComiendo1],[ConexionFilosofoPensando1,ConexionTenedor1,ConexionTenedor2],"Filosofo 1 deja de comer")
    T_Filosofo2DejaDeComer = Transition([ConexionFilosofoComiendo2],[ConexionFilosofoPensando2,ConexionTenedor2,ConexionTenedor3],"Filosofo 2 deja de comer")
    T_Filosofo3DejaDeComer = Transition([ConexionFilosofoComiendo3],[ConexionFilosofoPensando3,ConexionTenedor3,ConexionTenedor4],"Filosofo 3 deja de comer")
    T_Filosofo4DejaDeComer = Transition([ConexionFilosofoComiendo4],[ConexionFilosofoPensando4,ConexionTenedor4,ConexionTenedor5],"Filosofo 4 deja de comer")
    T_Filosofo5DejaDeComer = Transition([ConexionFilosofoComiendo5],[ConexionFilosofoPensando5,ConexionTenedor5,ConexionTenedor1],"Filosofo 5 deja de comer")

    aux = [T_Filosofo1Come,T_Filosofo2Come,T_Filosofo3Come,T_Filosofo4Come,T_Filosofo5Come,
    T_Filosofo1DejaDeComer,T_Filosofo2DejaDeComer,T_Filosofo3DejaDeComer,T_Filosofo4DejaDeComer,T_Filosofo5DejaDeComer]

    #Se inicializan los threads.
    for i in aux:
        i.start()

    for i in aux:
        i.join()

if __name__ == "__main__":
    main()
