
from Place import Place

class Connection:
    def __init__(self,place:Place,weight):
        #contiene el place de la conexion
        self.place = place
        # y el peso (weight) de la conexion
        self.weight = weight
        
    #Verifica si el place asignado tiene la cantidad necesaria de tokens
    def condition(self) -> bool:
        return self.place.tokens >= self.weight
            