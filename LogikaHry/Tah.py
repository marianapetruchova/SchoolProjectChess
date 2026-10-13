from typing import Tuple

from model.Figurka import Figurka


class Tah:
    def __init__(self, vychozi_pozice: Tuple[int, int], cilova_pozice: Tuple[int, int], figurka: Figurka,
                 typ_tahu: str = "normal"):
        self.vychozi_pozice = vychozi_pozice
        self.cilova_pozice = cilova_pozice
        self.figurka = figurka
        self.typ_tahu = typ_tahu

    def over_platnost(self) -> bool:
        return True if self.figurka == self.cilova_pozice else False

    def proved_tah(self):
        pass