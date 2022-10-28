
from Place import Place
from Transition import Transition


def main():
    aux1 = Place(1,1,0)
    aux2 = Transition(1,aux1)
    aux1.start()
    aux2.start()

if __name__ == "__main__":
    main()