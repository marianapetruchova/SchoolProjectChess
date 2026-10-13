from typing import List

from LogikaHry.HerniPlocha import HerniPlocha
from LogikaHry.Tah import Tah


class RevizorTahu:
    def __init__(self, herni_plocha: HerniPlocha, tah: Tah = None):
        self.herni_plocha = herni_plocha
        self.tah = tah

    def simulate_Move(self) -> List:
        return []

    def check_Sach(self) -> bool:
        return False

    def check_Mat(self) -> bool:
        return False

    def check_Pat(self) -> bool:
        return False