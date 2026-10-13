from model.Figurka import Figurka
from model.Vektor import Vektor


class Pesak(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Pěšák", barva)
        self.skok = False
        self.vektory = [Vektor(0, 1 * barva)]
        self.vektory_utoku = [Vektor(1, 1 * barva), Vektor(-1, 1 * barva)]