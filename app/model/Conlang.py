from dataclasses import dataclass


@dataclass
class Conlang:
    name: str = ""          # A nyelv neve
    words: list = list()    # Ez a lista tárolja a szavakat (Word típusban)
    wordcount: int = 0      # A szótár mérete

    def __str__(self):
        return f"{self.name} nyelv profilja | szótár mérete: {self.wordcount} szó"