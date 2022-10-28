
from Connections import Connection
from Place import Place
from Transition import Transition


def main():

    P1 = Place(1)
    P2 = Place(0)
    
    in1 = Connection(P1,1)
    out1 = Connection(P2,1)
    in2 = Connection(P2,1)
    out2 = Connection(P1,1)

    T1 = Transition({in1},{out1},"T1")
    T2 = Transition({in2},{out2},"T2")
    
    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print(P1.tokens)


if __name__ == "__main__":
    main()
