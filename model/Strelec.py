from model.Figurka import Figurka
from model.Vektor import Vektor


class Strelec(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Střelec", barva)
        self.skok = False
        self.vektory = [
            Vektor(1, 1), Vektor(-1, 1), Vektor(1, -1), Vektor(-1, -1)
        ]
        self.vektory_utoku = self.vektory