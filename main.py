# ==========================================
# 1. VEKTORY A FIGURKY
# ==========================================

class Vektor:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figurka:
    def __init__(self, nazev: str = "", barva: int = 1):
        self.nazev = nazev
        self.barva = barva  # 1 pro bílou, -1 pro černou
        self.vektory: List[Vektor] = []
        self.vektory_utoku: List[Vektor] = []
        self.skok: bool = False

    def get_barva(self) -> int:
        return self.barva


class Kun(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Kůň", barva)
        self.skok = True
        self.vektory = [
            Vektor(1, 2), Vektor(2, 1), Vektor(-1, 2), Vektor(-2, 1),
            Vektor(1, -2), Vektor(2, -1), Vektor(-1, -2), Vektor(-2, -1)
        ]
        self.vektory_utoku = self.vektory


class Kral(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Král", barva)
        self.skok = False
        self.vektory = [
            Vektor(1, 0), Vektor(-1, 0), Vektor(0, 1), Vektor(0, -1),
            Vektor(1, 1), Vektor(-1, 1), Vektor(1, -1), Vektor(-1, -1)
        ]
        self.vektory_utoku = self.vektory


class Dama(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Dáma", barva)
        self.skok = False
        self.vektory = [
            Vektor(1, 0), Vektor(-1, 0), Vektor(0, 1), Vektor(0, -1),
            Vektor(1, 1), Vektor(-1, 1), Vektor(1, -1), Vektor(-1, -1)
        ]
        self.vektory_utoku = self.vektory


class Vez(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Věž", barva)
        self.skok = False
        self.vektory = [
            Vektor(1, 0), Vektor(-1, 0), Vektor(0, 1), Vektor(0, -1)
        ]
        self.vektory_utoku = self.vektory


class Strelec(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Střelec", barva)
        self.skok = False
        self.vektory = [
            Vektor(1, 1), Vektor(-1, 1), Vektor(1, -1), Vektor(-1, -1)
        ]
        self.vektory_utoku = self.vektory


class Pesak(Figurka):
    def __init__(self, barva: int = 1):
        super().__init__("Pěšák", barva)
        self.skok = False
        self.vektory = [Vektor(0, 1 * barva)]
        self.vektory_utoku = [Vektor(1, 1 * barva), Vektor(-1, 1 * barva)]


# ==========================================
# 2. UŽIVATELÉ A QUESTY
# ==========================================

class Kwest:
    def __init__(self, nazev: str, popis: str):
        self.nazev = nazev
        self.popis = popis

    def validate(self) -> bool:
        return False


class Uzivatel:
    def __init__(self, uzivatelske_jmeno: str, jmeno: str, email: str, elo: int = 1200):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.jmeno = jmeno
        self.email = email
        self.elo = elo
        self.splnene_kwesty: List[Kwest] = []

    def pridej_quest(self, quest: Kwest) -> None:
        self.splnene_kwesty.append(quest)


class Hrac:
    def __init__(self, uzivatel: Uzivatel, barva: int):
        self.uzivatel = uzivatel
        self.barva = barva

    def get_elo_rating(self) -> int:
        return self.uzivatel.elo


# ==========================================
# 3. HERNÍ PLOCHA A TAHY
# ==========================================

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


# ==========================================
# 4. REVIZOR TAHU
# ==========================================

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


# ==========================================
# 5. SPRÁVA HRY (GAME MANAGER)
# ==========================================

class GameManager:
    def __init__(self, hrac1: Hrac, hrac2: Hrac):
        self.plocha = HerniPlocha()
        self.aktivni_hrac: int = 0
        self.hraci: List[Hrac] = [hrac1, hrac2]
        self.aktualni_tah: Optional[Tah] = None
        self.revizor_tahu = RevizorTahu(self.plocha)

    def najdi_uzivatele(self, user_id: int) -> Uzivatel:
        return self.hraci[0].uzivatel


# ==========================================
# SPUŠTĚNÍ PROGRAMU
# ==========================================

if __name__ == "__main__":
    print("Inicializace šachové aplikace...")

    u1 = Uzivatel("hrac_bily", "Jan", "jan@email.cz", elo=1350)
    u2 = Uzivatel("hrac_cerny", "Petr", "petr@email.cz", elo=1280)

    h1 = Hrac(u1, barva=1)
    h2 = Hrac(u2, barva=-1)

    hra = GameManager(h1, h2)

    print(
        f"Hra připravena: {h1.uzivatel.jmeno} (ELO {h1.get_elo_rating()}) vs {h2.uzivatel.jmeno} (ELO {h2.get_elo_rating()})")
    print("Vše proběhlo úspěšně bez chyb!")