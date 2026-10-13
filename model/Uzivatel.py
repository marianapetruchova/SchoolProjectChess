from typing import List

from model.Quest import Quest


class Uzivatel:
    def __init__(self, uzivatelske_jmeno: str, jmeno: str, email: str, elo: int = 1200):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.jmeno = jmeno
        self.email = email
        self.elo = elo
        self.splnene_kwesty: List[Quest] = []

    def pridej_quest(self, quest: Quest) -> None:
        self.splnene_kwesty.append(quest)