from src.text.parser import Parser
from src.structure.set import Set
class Vertex:
    """Lightweight vertex structure for a graph."""
    def __init__(self, ime, linkovi, reci):
        self.ime = ime                        #putanja linka
        self.linkovi = linkovi                  #linkovi na koje pokazuje ovaj cvor
        self.reci = reci                        #reci iz linka
        self.veze = Set()                       #skup cvorova koji pokazuju na ovaj cvor

    """def element(self):
        Return element associated with this vertex.
        return self._element"""

    def parsiraj(self):
        parserr = Parser()                      #metoda za parsiranje unete putanje
        return parserr.parse(self.ime)

    """def __hash__(self): # will allow vertex to be a map/set key
        return hash(id(self))
    def __str__(self):
        return str(self._element)"""