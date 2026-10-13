from controller.Controller import Controller
from model.Hrac import Hrac
from model.Uzivatel import Uzivatel

class GameManager:
    pass


if __name__ == "__main__":
    print("Inicializace šachové aplikace...")

    u1 = Uzivatel("hrac_bily", "Jan", "jan@email.cz", elo=1350)
    u2 = Uzivatel("hrac_cerny", "Petr", "petr@email.cz", elo=1280)

    h1 = Hrac(u1, barva=1)
    h2 = Hrac(u2, barva=-1)

    hra = Controller(h1, h2)

    print(
        f"Hra připravena: {h1.uzivatel.jmeno} (ELO {h1.get_elo_rating()}) vs {h2.uzivatel.jmeno} (ELO {h2.get_elo_rating()})")
    print("Vše proběhlo úspěšně bez chyb!")