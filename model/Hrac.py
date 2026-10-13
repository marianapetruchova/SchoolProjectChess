from model.Uzivatel import Uzivatel


class Hrac:
    def __init__(self, uzivatel: Uzivatel, barva: int):
        self.uzivatel = uzivatel
        self.barva = barva

    def get_elo_rating(self) -> int:
        return self.uzivatel.elo