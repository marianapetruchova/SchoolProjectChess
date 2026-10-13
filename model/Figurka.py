from typing import List


class Figurka:
    def __init__(self, nazev: str = "", barva: int = 1):
        self.nazev = nazev
        self.barva = barva  # 1 pro bílou, -1 pro černou
        self.vektory: List[Vektor] = []
        self.vektory_utoku: List[Vektor] = []
        self.skok: bool = False

    def get_barva(self) -> int:
        return self.barva