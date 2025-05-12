from dataclasses import dataclass


@dataclass
class Word:
    original: str               # Az adott szó szótári alakban
    language: str               # A nyelv, amihez tartozik a szó
    translation: list = list()  # Egy lista, ami angol megfelelőket tartalmaz


    def __str__(self):
        return f"Word(original={self.original}, language={self.language}, translation={self.translation})"