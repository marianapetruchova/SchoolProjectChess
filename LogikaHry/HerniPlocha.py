from typing import Tuple, List, Optional

from LogikaHry.Tah import Tah
from model.Figurka import Figurka


class HerniPlocha:
    def __init__(self):
        self.rozmery: Tuple[int, int] = (8, 8)
        self.herni_deska: List[List[Optional[Figurka]]] = [[None for _ in range(8)] for _ in range(8)]
        self.vyhozene_figurky_b: List[Figurka] = []
        self.vyhozene_figurky_c: List[Figurka] = []

    def vrat_obsah(self, souradnice: Tuple[int, int]) -> Optional[Figurka]:
        x, y = souradnice
        if 0 <= x < 8 and 0 <= y < 8:
            return self.herni_deska[x][y]
        return None

    def posun_figurky(self, tah: Tah) -> bool:
        x1, y1 = tah.vychozi_pozice
        x2, y2 = tah.cilova_pozice
        figurka = self.herni_deska[x1][y1]

        if figurka:
            cilova_fig = self.herni_deska[x2][y2]
            if cilova_fig:
                self.vyhozene_figurky_b.append(cilova_fig)
            self.herni_deska[x2][y2] = figurka
            self.herni_deska[x1][y1] = None
            return True
        return False

    def nahrad_figurku(self, figurka: Figurka, tah: Tah) -> None:
        x, y = tah.cilova_pozice
        self.herni_deska[x][y] = figurka