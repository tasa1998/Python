from parser1 import Parser
class Vertex:
    """Lightweight vertex structure for a graph."""
    def __init__(self, ime, linkovi, reci):
        self.ime=ime
        self.linkovi=linkovi
        self.reci=reci
        self.veze=set() #skup cvorova koji pokazuju na ovaj cvor

    """def element(self):
        Return element associated with this vertex.
        return self._element"""

    def parsiraj(self):
        parserr=Parser()
        return parserr.parse(self.ime)

    """def __hash__(self): # will allow vertex to be a map/set key
        return hash(id(self))
    def __str__(self):
        return str(self._element)"""