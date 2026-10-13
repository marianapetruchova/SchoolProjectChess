from typing import List, Optional

from LogikaHry.HerniPlocha import HerniPlocha
from LogikaHry.RevizorTahu import RevizorTahu
from LogikaHry.Tah import Tah
from model.Hrac import Hrac
from model.Uzivatel import Uzivatel


class Controller:
    def __init__(self, hrac1: Hrac, hrac2: Hrac):
        self.plocha = HerniPlocha()
        self.aktivni_hrac: int = 0
        self.hraci: List[Hrac] = [hrac1, hrac2]
        self.aktualni_tah: Optional[Tah] = None
        self.revizor_tahu = RevizorTahu(self.plocha)

    def najdi_uzivatele(self, user_id: int) -> Uzivatel:
        return self.hraci[0].uzivatel