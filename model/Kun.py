from model.Figurka import Figurka
from model.Vektor import Vektor


class Kun(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Kůň", barva)
        self.skok = True
        self.vektory = [
            Vektor(1, 2), Vektor(2, 1), Vektor(-1, 2), Vektor(-2, 1),
            Vektor(1, -2), Vektor(2, -1), Vektor(-1, -2), Vektor(-2, -1)
        ]
        self.vektory_utoku = self.vektory