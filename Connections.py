
from Place import Place


class Connection:
    def __init__(self,place:Place,weight):
        self.place = place
        self.weight = weight

    def condition(self) -> bool:
        return self.place.tokens >= self.weight
            