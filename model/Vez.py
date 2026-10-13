from model.Figurka import Figurka
from model.Vektor import Vektor


class Vez(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Věž", barva)
        self.skok = False
        self.vektory = [
            Vektor(1, 0), Vektor(-1, 0), Vektor(0, 1), Vektor(0, -1)
        ]
        self.vektory_utoku = self.vektory